from fastapi import APIRouter, HTTPException, Depends
from app.database import db
from app.auth import get_user
from bson import ObjectId
from app.schemas import AddToCartSchema

router = APIRouter()

@router.post("/add")
async def add_to_cart(data: AddToCartSchema, current_user=Depends(get_user)):
    product = await db["products"].find_one({"_id": ObjectId(data.product_id)})
    if not product:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    if data.quantity <= 0 or data.quantity > product["quantity"]:
        raise HTTPException(status_code=400, detail="Cantidad no válida")
    
    cart_item = {
        "user": current_user["username"],
        "product_id": data.product_id,
        "quantity": data.quantity
    }
    await db["carts"].insert_one(cart_item)
    return {"msg": "Producto añadido al carrito"}
