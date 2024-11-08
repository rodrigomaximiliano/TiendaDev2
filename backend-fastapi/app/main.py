
from fastapi import FastAPI
from app.auth import router as auth_router
from app.product import router as product_router
from app.admin import router as admin_router
from app.cart import router as cart_router
from app.order import router as order_router
from app.mi_cuenta import router as mi_cuenta_router
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router, prefix="/auth")
app.include_router(product_router, prefix="/store")
app.include_router(admin_router, prefix="/admin")
app.include_router(cart_router, prefix="/cart")
app.include_router(order_router, prefix="/orders")
app.include_router(mi_cuenta_router, prefix="/mi_cuenta")

