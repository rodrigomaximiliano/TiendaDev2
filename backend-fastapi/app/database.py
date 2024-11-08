from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv

load_dotenv()

# Carga la URI desde el archivo .env
MONGODB_URI = os.getenv("MONGODB_URI")

# Inicializa el cliente de MongoDB
client = AsyncIOMotorClient(MONGODB_URI)
db = client["my_store_db"]
