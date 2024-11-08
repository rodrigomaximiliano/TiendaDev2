from fastapi import APIRouter, Depends, HTTPException
from app.database import db
from app.auth import get_user

router = APIRouter()

@router.get("/mi_cuenta")
async def get_profile(current_user=Depends(get_user)):
    return {"username": current_user["username"], "reputation": current_user.get("reputation", 0)}

@router.put("/mi_cuenta")
async def update_profile(update_data: dict, current_user=Depends(get_user)):
    if "username" in update_data and update_data["username"] != current_user["username"]:
        raise HTTPException(status_code=400, detail="Cannot update other user's profile")
    
    await db["users"].update_one({"username": current_user["username"]}, {"$set": update_data})
    return {"msg": "Profile updated successfully"}