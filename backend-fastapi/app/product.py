import datetime
from fastapi import APIRouter, HTTPException, Depends
from app.database import db
from app.schemas import AddToCartSchema, ProductSchema
from app.auth import get_user
from bson import ObjectId
from typing import Optional
from pydantic import validator

router = APIRouter()

# Serializar los productos para la respuesta
def product_serializer(product) -> dict:
    return {
        "id": str(product["_id"]),
        "name": product.get("name"),
        "description": product.get("description"),
        "price": product.get("price"),
        "quantity": product.get("quantity"),
        "seller": product.get("seller"),
    }

# Endpoint para crear un nuevo producto
@router.post("/create")
async def create_product(product: ProductSchema, current_user=Depends(get_user)):
    # Validación de precio y cantidad
    if product.price <= 0:
        raise HTTPException(status_code=400, detail="El precio debe ser positivo")
    if product.quantity < 0:
        raise HTTPException(status_code=400, detail="La cantidad no puede ser negativa")
    
    # Preparar los datos para la inserción
    product_data = product.dict()
    product_data["seller"] = current_user["username"]
    
    # Insertar el producto en la base de datos
    await db["products"].insert_one(product_data)
    return {"msg": "Producto creado exitosamente"}

# Endpoint para listar los productos con filtros y paginación
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

    # Obtener el número total de productos que cumplen con los filtros
    total_products = await db["products"].count_documents(query)
    
    # Obtener los productos con paginación
    products = await db["products"].find(query).skip((page - 1) * limit).limit(limit).to_list(length=limit)
    
    # Devolver los productos con la información de paginación
    return {
        "total_products": total_products,
        "page": page,
        "limit": limit,
        "products": [product_serializer(product) for product in products]
    }


