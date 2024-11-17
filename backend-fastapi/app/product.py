import os
from typing import Optional
from fastapi import APIRouter, HTTPException, Depends, File, UploadFile
from app.database import db
from app.schemas import ProductSchema
from app.auth import get_user
from bson import ObjectId

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
async def create_product(product: ProductSchema, current_user=Depends(get_user)):
    if product.price <= 0:
        raise HTTPException(status_code=400, detail="El precio debe ser positivo")
    if product.quantity < 0:
        raise HTTPException(status_code=400, detail="La cantidad no puede ser negativa")
    
    product_data = product.dict()
    product_data["seller"] = current_user["username"]
    
    await db["products"].insert_one(product_data)
    return {"msg": "Producto creado exitosamente"}

@router.post("/upload_image")
async def upload_image(file: UploadFile = File(...)):
    file_location = f"app/static/images/{file.filename}"
    
    try:
        with open(file_location, "wb") as f:
            f.write(file.file.read())
    except Exception:
        raise HTTPException(status_code=500, detail="Error al guardar la imagen")

    return {"imagen": f"/static/images/{file.filename}"}

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

@router.put("/update/{product_id}")
async def update_product(
    product_id: str, 
    product_update: ProductSchema, 
    current_user=Depends(get_user)
):
    product = await db["products"].find_one({"_id": ObjectId(product_id)})
    if not product:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    
    if product["seller"] != current_user["username"]:
        raise HTTPException(status_code=403, detail="No tienes permiso para actualizar este producto")
    
    if product_update.price <= 0:
        raise HTTPException(status_code=400, detail="El precio debe ser positivo")
    if product_update.quantity < 0:
        raise HTTPException(status_code=400, detail="La cantidad no puede ser negativa")
    
    updated_data = product_update.dict(exclude_unset=True)
    await db["products"].update_one({"_id": ObjectId(product_id)}, {"$set": updated_data})
    return {"msg": "Producto actualizado exitosamente"}

@router.delete("/delete/{product_id}")
async def delete_product(product_id: str, current_user=Depends(get_user)):
    product = await db["products"].find_one({"_id": ObjectId(product_id)})
    if not product:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    
    if product["seller"] != current_user["username"]:
        raise HTTPException(status_code=403, detail="No tienes permiso para eliminar este producto")
    
    await db["products"].delete_one({"_id": ObjectId(product_id)})
    return {"msg": "Producto eliminado exitosamente"}
