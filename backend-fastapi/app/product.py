import os
from typing import Optional
from fastapi import APIRouter, HTTPException, Depends, File, UploadFile
from app.database import db
from app.auth import get_user
from bson import ObjectId
from fastapi import Form

router = APIRouter()

os.makedirs("app/static/images", exist_ok=True)

def product_serializer(product) -> dict:
    return {
        "id": str(product["_id"]),
        "name": product.get("name"),
        "description": product.get("description"),
        "price": product.get("price"),
        "quantity": product.get("quantity"),
        "seller": product.get("seller"),
        "imagen": product.get("imagen"),
    }

@router.post("/create")
async def create_product_with_image(
    name: str = Form(...),
    description: str = Form(...),
    price: float = Form(...),
    quantity: int = Form(...),
    file: UploadFile = File(...), 
    current_user=Depends(get_user),
):
    if price <= 0:
        raise HTTPException(status_code=400, detail="El precio debe ser positivo")
    if quantity < 0:
        raise HTTPException(status_code=400, detail="La cantidad no puede ser negativa")

    # Guardar la imagen
    file_location = f"app/static/images/{file.filename}"
    try:
        with open(file_location, "wb") as f:
            f.write(file.file.read())
    except Exception:
        raise HTTPException(status_code=500, detail="Error al guardar la imagen")

    # Crear el producto
    product_data = {
        "name": name,
        "description": description,
        "price": price,
        "quantity": quantity,
        "seller": current_user["username"],
        "imagen": f"/static/images/{file.filename}",
    }
    await db["products"].insert_one(product_data)
    return {"msg": "Producto creado exitosamente"}

@router.get("/products")
async def list_products(
    page: int = 1,
    limit: int = 10,
    min_price: Optional[float] = None,
    max_price: Optional[float] = None,
):
    query = {}
    if min_price is not None:
        query["price"] = {"$gte": min_price}
    if max_price is not None:
        query.setdefault("price", {})
        query["price"]["$lte"] = max_price

    total_products = await db["products"].count_documents(query)
    
    products = await db["products"].find(query).skip((page - 1) * limit).limit(limit).to_list(length=limit)
    
    return {
        "total_products": total_products,
        "page": page,
        "limit": limit,
        "products": [product_serializer(product) for product in products]
    }

@router.get("/my-products")
async def get_user_products(current_user=Depends(get_user)):
    products = await db["products"].find({"seller": current_user["username"]}).to_list(length=None)
    
    if not products:
        raise HTTPException(status_code=404, detail="No se encontraron productos para este usuario")

    return {
        "products": [product_serializer(product) for product in products]
    }

@router.delete("/products/{product_id}")
async def delete_product(product_id: str, current_user=Depends(get_user)):
    product = await db["products"].find_one({"_id": ObjectId(product_id)})
    if not product:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    if product["seller"] != current_user["username"]:
        raise HTTPException(status_code=403, detail="No tienes permiso para eliminar este producto")

    result = await db["products"].delete_one({"_id": ObjectId(product_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=500, detail="Error al eliminar el producto")
    
    return {"msg": "Producto eliminado exitosamente"}

@router.put("/products/{product_id}")
async def edit_product(
    product_id: str,
    name: Optional[str] = Form(None),
    description: Optional[str] = Form(None),
    price: Optional[float] = Form(None),
    quantity: Optional[int] = Form(None),
    file: Optional[UploadFile] = File(None),
    current_user=Depends(get_user)
):
    product = await db["products"].find_one({"_id": ObjectId(product_id)})
    if not product:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    if product["seller"] != current_user["username"]:
        raise HTTPException(status_code=403, detail="No tienes permiso para editar este producto")

    update_data = {}
    if name:
        update_data["name"] = name
    if description:
        update_data["description"] = description
    if price is not None:
        update_data["price"] = price
    if quantity is not None:
        update_data["quantity"] = quantity
    if file:
        file_location = f"app/static/images/{file.filename}"
        try:
            with open(file_location, "wb") as f:
                f.write(file.file.read())
        except Exception:
            raise HTTPException(status_code=500, detail="Error al guardar la nueva imagen")
        update_data["imagen"] = f"/static/images/{file.filename}"

    result = await db["products"].update_one(
        {"_id": ObjectId(product_id)},
        {"$set": update_data}
    )
    
    if result.modified_count == 0:
        raise HTTPException(status_code=500, detail="Error al actualizar el producto")

    return {"msg": "Producto actualizado exitosamente"}
