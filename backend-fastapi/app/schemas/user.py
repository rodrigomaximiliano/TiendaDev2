from pydantic import BaseModel, EmailStr

class UserSchema(BaseModel):
    username: str
    password: str

class UserCreateSchema(UserSchema):
    email: EmailStr
