from fastapi import APIRouter, HTTPException, Depends
from app.database import db
from app.auth import get_user
from bson import ObjectId

router = APIRouter()

@router.post("/create")
async def create_order(current_user=Depends(get_user)):
    cart_items = await db["carts"].find({"user": current_user["username"]}).to_list(length=100)
    if not cart_items:
        raise HTTPException(status_code=400, detail="Cart is empty")

    total_price = 0
    for item in cart_items:
        product = await db["products"].find_one({"_id": ObjectId(item["product_id"])})
        total_price += product["price"] * item["quantity"]
        await db["products"].update_one({"_id": ObjectId(item["product_id"])}, {"$inc": {"quantity": -item["quantity"]}})

    order_data = {
        "user": current_user["username"],
        "items": cart_items,
        "total_price": total_price,
        "status": "pending"
    }
    await db["orders"].insert_one(order_data)
    await db["carts"].delete_many({"user": current_user["username"]})  # Vaciar carrito después de la compra
    return {"msg": "Order created successfully", "total_price": total_price}

