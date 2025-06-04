from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.routers import admin, auth, cart, order, product, user, mi_cuenta

app = FastAPI(title=settings.PROJECT_NAME)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(cart.router, prefix="/cart", tags=["cart"])
app.include_router(mi_cuenta.router, prefix="/mi-cuenta", tags=["mi-cuenta"])
app.include_router(admin.router, prefix="/admin", tags=["admin"])
app.include_router(order.router, prefix="/order", tags=["order"])
app.include_router(product.router, prefix="/product", tags=["product"])
app.include_router(user.router, prefix="/user", tags=["user"])

