from fastapi import APIRouter, HTTPException, Depends
from app.database import db
from app.schemas import ProductSchema
from bson import ObjectId
from app.auth import get_user
from typing import Optional
from pydantic import condecimal

router = APIRouter()

def product_serializer(product) -> dict:
    return {
        "id": str(product["_id"]),
        "name": product.get("name"),
        "description": product.get("description"),
        "price": product.get("price"),
        "quantity": product.get("quantity"),
        "seller": product.get("seller"),
    }

@router.post("/product")
async def create_product(product: ProductSchema, current_user=Depends(get_user)):
    if product.price <= 0:
        raise HTTPException(status_code=400, detail="Price must be positive")
    if product.quantity < 0:
        raise HTTPException(status_code=400, detail="Quantity cannot be negative")
    
    product_data = product.dict()
    product_data["seller"] = current_user["username"]
    await db["products"].insert_one(product_data)
    return {"msg": "Product created successfully"}

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

    products = await db["products"].find(query).skip((page - 1) * limit).limit(limit).to_list(length=limit)
    return [product_serializer(product) for product in products]