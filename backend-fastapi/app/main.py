from fastapi import FastAPI, Depends, HTTPException
from app.auth import router as auth_router, verify_token 
from app.product import router as product_router
from app.admin import router as admin_router
from app.cart import router as cart_router
from app.order import router as order_router
from app.mi_cuenta import router as mi_cuenta_router
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv
from fastapi.staticfiles import StaticFiles

load_dotenv()

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
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


app.mount("/static", StaticFiles(directory="app/static"), name="static")
