from fastapi import FastAPI
from pydantic import BaseModel, Field, EmailStr

app = FastAPI()

class User(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    age: int = Field(gt=0, lt=120)
    email: EmailStr


@app.post("/user")
def create_user(user: User):
    return {
        "message": "User created successfully",
        "data": user
    }