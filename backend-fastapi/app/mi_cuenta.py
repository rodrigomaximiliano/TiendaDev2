from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from app.database import db
from app.auth import get_user  # Aquí se debe usar tu función de autenticación.
from pydantic import BaseModel, EmailStr
from typing import Optional
import os
from uuid import uuid4
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi import Form

# Definir el esquema para la actualización del perfil (sin bio)
class UpdateProfileRequest(BaseModel):
    full_name: Optional[str] = None
    email: Optional[EmailStr] = None
    photo_url: Optional[str] = None  # Para almacenar la URL de la foto

router = APIRouter()

# Función para guardar la imagen en el sistema o almacenamiento
def save_image(image: UploadFile) -> str:
    # Obtener el nombre único para la imagen
    extension = image.filename.split(".")[-1]
    image_name = f"{uuid4()}.{extension}"
    
    # Definir el directorio donde se almacenarán las imágenes
    upload_dir = "app/static/images"
    os.makedirs(upload_dir, exist_ok=True)
    
    image_path = os.path.join(upload_dir, image_name)
    
    # Guardar el archivo de la imagen en el servidor
    with open(image_path, "wb") as buffer:
        buffer.write(image.file.read())
    
    # Retornar la URL accesible de la imagen
    return f"/static/images/{image_name}"

# Endpoint para obtener el perfil del usuario
@router.get("/mi_cuenta")
async def get_profile(username: str, current_user=Depends(get_user)):
    # Verificar que el username del perfil solicitado sea el mismo que el del usuario autenticado
    if username != current_user["username"]:
        raise HTTPException(status_code=403, detail="You are not authorized to view this profile")

    user = await db["users"].find_one({"username": username})
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Devolver los datos del usuario
    return {
        "username": user["username"],
        "full_name": user.get("full_name", ""),
        "email": user.get("email", ""),
        "reputation": user.get("reputation", 0),  # Solo se muestra, no se puede actualizar
        "photo_url": user.get("photo_url", "/static/images/default-avatar.png")  # URL de la foto de perfil
    }

# Endpoint para actualizar el perfil del usuario, incluyendo foto de perfil
@router.put("/mi_cuenta")
async def update_profile(
    full_name: str = Form(...),
    email: EmailStr = Form(...),
    username: str = Form(...),
    current_user=Depends(get_user),
    photo: UploadFile = File(None)
):
    # Verificar que el username del perfil solicitado sea el mismo que el del usuario autenticado
    if username != current_user["username"]:
        raise HTTPException(status_code=403, detail="You are not authorized to update this profile")

    # Verificar si el usuario existe en la base de datos
    user = await db["users"].find_one({"username": username})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Preparar los datos para actualizar
    update_data = {
        "full_name": full_name,
        "email": email,
    }

    # Si el usuario sube una foto, guardarla y actualizar el campo photo_url
    if photo:
        photo_url = save_image(photo)
        update_data["photo_url"] = photo_url  # Actualizar la URL de la foto en los datos
    
    # Filtrar los datos a actualizar
    await db["users"].update_one(
        {"username": username}, 
        {"$set": update_data}
    )
    
    # Devolver una respuesta con los datos actualizados
    return JSONResponse(
        content=jsonable_encoder({
            "msg": "Profile updated successfully",
            "updated_fields": update_data,
            "photo_url": update_data.get("photo_url", "")
        }),
        status_code=200
    )
