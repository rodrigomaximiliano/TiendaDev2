from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv

load_dotenv()


MONGODB_URI = os.getenv("MONGODB_URI")


client = AsyncIOMotorClient(MONGODB_URI)
db = client["my_store_db"]
