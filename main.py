from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Fake in-memory database
fake_db = []

# Schema for user
class User(BaseModel):
    id: int
    name: str
    email: str

# Get all users
@app.get("/users")
def get_users():
    return {"name":"John Doe", "email":"abc@gmail.com","sal":"1000"}




 



