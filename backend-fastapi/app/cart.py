import os
from fastapi import APIRouter, HTTPException, Depends
from app.database import db
from app.schemas import AddToCartSchema, CartItemResponse
from app.auth import get_user
from bson import ObjectId
import datetime
import logging

router = APIRouter()

# Logger for debugging purposes
logger = logging.getLogger(__name__)

# Helper function to validate ObjectId format
def is_valid_objectid(id_str: str) -> bool:
    return len(id_str) == 24 and all(c in '0123456789abcdef' for c in id_str.lower())


@router.post("/add")
async def add_to_cart(data: AddToCartSchema, current_user=Depends(get_user)):
    # Validate product_id format
    if not is_valid_objectid(data.product_id):
        logger.error(f"Invalid product ID format: {data.product_id}")
        raise HTTPException(status_code=400, detail="ID de producto inválido")
    
    try:
        product_id = ObjectId(data.product_id)
    except Exception as e:
        logger.error(f"Error converting product ID: {data.product_id}")
        raise HTTPException(status_code=400, detail="ID de producto inválido")
    
    # Check if product exists
    product = await db["products"].find_one({"_id": product_id})
    if not product:
        logger.error(f"Product not found: {data.product_id}")
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    
    # Validate product quantity
    if "quantity" not in product or product["quantity"] <= 0:
        raise HTTPException(status_code=404, detail="Producto no disponible")
    
    if data.quantity <= 0 or data.quantity > product["quantity"]:
        logger.error(f"Invalid quantity: {data.quantity} for product {product_id}")
        raise HTTPException(status_code=400, detail="Cantidad no válida")
    
    # Cart item to add or update
    cart_item = {
        "user_id": current_user["_id"],
        "product_id": product_id,
        "quantity": data.quantity,
        "added_at": datetime.datetime.utcnow()
    }
    
    # Check if the item already exists in the cart
    existing_cart_item = await db["carts"].find_one({"user_id": current_user["_id"], "product_id": product_id})
    
    if existing_cart_item:
        # Update existing cart item quantity
        new_quantity = existing_cart_item["quantity"] + data.quantity
        if new_quantity > product["quantity"]:
            raise HTTPException(status_code=400, detail="No hay suficiente stock para esta cantidad")
        
        await db["carts"].update_one(
            {"_id": existing_cart_item["_id"]},
            {"$set": {"quantity": new_quantity}}
        )
    else:
        # Add new item to the cart
        await db["carts"].insert_one(cart_item)
    
    return {"msg": "Producto añadido al carrito"}


@router.get("/view")
async def view_cart(current_user=Depends(get_user)):
    # Get all cart items for the user
    cart_items = await db["carts"].find({"user_id": current_user["_id"]}).to_list(length=100)
    
    if not cart_items:
        return {"msg": "El carrito está vacío"}
    
    # Get product details for each item in the cart
    product_ids = [item["product_id"] for item in cart_items]
    products = await db["products"].find({"_id": {"$in": product_ids}}).to_list(length=100)
    
    # Map cart items to product details
    cart_details = []
    for cart_item in cart_items:
        product = next((prod for prod in products if str(prod["_id"]) == str(cart_item["product_id"])), None)
        if product:
            cart_details.append({
                "product_id": str(cart_item["product_id"]),
                "name": product["name"],
                "price": product["price"],
                "quantity": cart_item["quantity"],
                "total_price": product["price"] * cart_item["quantity"],
                "imagen": product.get("imagen")  # Incluyendo imagen del producto
            })
    
    return {"cart": cart_details}


@router.delete("/remove")
async def remove_from_cart(product_id: str, current_user=Depends(get_user)):
    # Validate product_id format
    if not is_valid_objectid(product_id):
        logger.error(f"Invalid product ID format: {product_id}")
        raise HTTPException(status_code=400, detail="ID de producto inválido")
    
    try:
        product_id = ObjectId(product_id)
    except Exception:
        logger.error(f"Error converting product ID: {product_id}")
        raise HTTPException(status_code=400, detail="ID de producto inválido")
    
    # Check if the product is in the user's cart
    cart_item = await db["carts"].find_one({"user_id": current_user["_id"], "product_id": product_id})
    
    if not cart_item:
        logger.error(f"Product {product_id} not found in cart for user {current_user['_id']}")
        raise HTTPException(status_code=404, detail="Producto no encontrado en el carrito")
    
    # Delete the product from the cart
    delete_result = await db["carts"].delete_one({"_id": cart_item["_id"]})
    
    if delete_result.deleted_count == 0:
        logger.error(f"Failed to delete product {product_id} from cart")
        raise HTTPException(status_code=500, detail="Error al eliminar el producto del carrito")
    
    return {"msg": "Producto eliminado del carrito"}
