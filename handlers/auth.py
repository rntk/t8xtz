from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from typing import Optional
import jwt

SECRET_KEY = "your_secret_key"

auth_router = APIRouter()

class User(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

def create_access_token(data: dict):
    return jwt.encode(data, SECRET_KEY, algorithm="HS256")

@auth_router.post("/login", response_model=Token)
async def login(user: User):
    # This is a placeholder for actual authentication logic
    if user.username == "test" and user.password == "test":
        access_token = create_access_token(data={"sub": user.username})
        return {"access_token": access_token, "token_type": "bearer"}
    else:
        raise HTTPException(status_code=400, detail="Invalid credentials")

@auth_router.post("/register")
async def register(user: User):
    # This is a placeholder for actual registration logic
    return {"message": "User registered successfully"}
