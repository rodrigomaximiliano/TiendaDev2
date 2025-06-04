from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv
from .config import settings

load_dotenv()

client = AsyncIOMotorClient(settings.MONGODB_URI)
db = client.tiendadev

# Collections
users = db.users
products = db.products
orders = db.orders
carts = db.carts
