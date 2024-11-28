from fastapi import APIRouter, HTTPException, Depends
from app.database import db
from app.auth import get_user
from bson import ObjectId

router = APIRouter()

@router.post("/create")
async def create_order(address: str, paymentMethod: str, items: list, card_number: str, current_user=Depends(get_user)):
    # Verificar si el carrito tiene productos
    if not items:
        raise HTTPException(status_code=400, detail="El carrito está vacío")
    
    total_price = 0
    sold_products = []

    # Verificar y procesar los productos de la orden
    for item in items:
        product = await db["products"].find_one({"_id": ObjectId(item["product_id"])})
        if not product:
            raise HTTPException(status_code=404, detail="Producto no encontrado")

        total_price += product["price"] * item["quantity"]
        sold_products.append({
            "product_id": product["_id"],
            "product_name": product["name"],
            "price": product["price"],
            "quantity": item["quantity"],
            "total_price": product["price"] * item["quantity"]
        })
        
        # Actualizar la cantidad del producto en inventario
        await db["products"].update_one(
            {"_id": ObjectId(item["product_id"])},
            {"$inc": {"quantity": -item["quantity"]}}
        )

    # El proceso de pago es simulado y siempre es exitoso
    payment_success = True  # Pago siempre exitoso

    if not payment_success:
        raise HTTPException(status_code=400, detail="Error en el pago. Intenta nuevamente.")

    # Crear la orden
    order_data = {
        "user": current_user["username"],
        "items": sold_products,
        "total_price": total_price,
        "status": "pendiente",
        "address": address,
        "payment_method": paymentMethod,
        "card_number": card_number  # Guardar el número de tarjeta de forma simulada
    }

    # Insertar la orden en la base de datos
    await db["orders"].insert_one(order_data)
    
    # Limpiar el carrito
    await db["carts"].delete_many({"user": current_user["username"]})

    return {"msg": "Orden creada exitosamente", "total_price": total_price}
@router.get("/orders")
async def get_orders(current_user=Depends(get_user)):
    # Buscar todas las órdenes del usuario actual
    user_orders = await db["orders"].find({"user": current_user["username"]}).to_list(length=None)
    
    if not user_orders:
        raise HTTPException(status_code=404, detail="No se encontraron órdenes para este usuario")
    
    # Formatear los datos de las órdenes (opcional)
    formatted_orders = []
    for order in user_orders:
        formatted_orders.append({
            "id": str(order["_id"]),
            "total_price": order["total_price"],
            "status": order["status"],
            "items": order["items"],
            "address": order["address"],
            "payment_method": order["payment_method"],
            "created_at": order.get("created_at")  # Si guardas la fecha de creación
        })

    return {"orders": formatted_orders}
