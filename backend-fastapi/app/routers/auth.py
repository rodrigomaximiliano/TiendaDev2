from fastapi import APIRouter, HTTPException, Depends
from core.database import db
from schemas.user import UserSchema, UserCreateSchema
from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import jwt, JWTError
from fastapi.security import OAuth2PasswordBearer

# Configuración de la clave secreta y algoritmo para JWT
SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
router = APIRouter()


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})  # Añadir el tiempo de expiración
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(status_code=403, detail="Token is invalid or expired")


async def get_user(username: str):
    return await db["users"].find_one({"username": username})


async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = verify_token(token)  
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=403, detail="Could not validate credentials")
        user = await get_user(username)
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return user
    except JWTError:
        raise HTTPException(status_code=403, detail="Token is invalid or expired")
# Ruta para el login
@router.post("/login")
async def login(user: UserSchema):
    db_user = await get_user(user.username)
    if not db_user or not pwd_context.verify(user.password, db_user["password"]):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    
    # Crear token para el usuario
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer", "username": db_user["username"]}


@router.post("/register")
async def register(user: UserCreateSchema):
    db_user = await get_user(user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    
    hashed_password = pwd_context.hash(user.password)
    
    new_user = {
        "username": user.username,
        "password": hashed_password,
        "email": user.email,
        "created_at": datetime.utcnow(),
    }
    
    
    await db["users"].insert_one(new_user)
    
    return {"message": "User registered successfully"}