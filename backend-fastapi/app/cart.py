from fastapi import APIRouter, HTTPException, Depends
from app.database import db
from app.auth import get_user
from app.schemas import ProductSchema
from bson import ObjectId

router = APIRouter()

@router.get("/")
async def get_cart(current_user=Depends(get_user)):
    cart_items = await db["carts"].find({"user": current_user["username"]}).to_list(length=100)
    return {"cart": cart_items}

@router.post("/add")
async def add_to_cart(product_id: str, quantity: int, current_user=Depends(get_user)):
    product = await db["products"].find_one({"_id": ObjectId(product_id)})
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    if quantity <= 0 or quantity > product["quantity"]:
        raise HTTPException(status_code=400, detail="Invalid quantity")
    
    cart_item = {
        "user": current_user["username"],
        "product_id": product_id,
        "quantity": quantity
    }
    await db["carts"].insert_one(cart_item)
    return {"msg": "Product added to cart"}

@router.post("/remove")
async def remove_from_cart(cart_id: str, current_user=Depends(get_user)):
    cart_item = await db["carts"].find_one({"_id": ObjectId(cart_id), "user": current_user["username"]})
    if not cart_item:
        raise HTTPException(status_code=404, detail="Cart item not found")
    
    await db["carts"].delete_one({"_id": ObjectId(cart_id)})
    return {"msg": "Product removed from cart"}
