from fastapi import APIRouter, HTTPException, Depends
from app.database import db
from app.auth import get_user

router = APIRouter()

@router.put("/user/{username}")
async def update_user_profile(username: str, update_data: dict, current_user=Depends(get_user)):
    if current_user["role"] != "admin":
        raise HTTPException(status_code=403, detail="Operation not permitted")

    user = await db["users"].find_one({"username": username})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    await db["users"].update_one({"username": username}, {"$set": update_data})
    return {"msg": "User profile updated successfully"}

