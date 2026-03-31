from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# ===== GET =====
@app.get("/hello")
def say_hello(name: str, age: int):
    return {
        "message": f"Hello {name}",
        "age": age
    }


# ===== POST (query params - cách 1) =====
@app.post("/sum")
def calculate_sum(a: int, b: int):
    return {
        "a": a,
        "b": b,
        "result": a + b
    }


# ===== POST (body - cách 2) =====
class SumRequest(BaseModel):
    a: int
    b: int


@app.post("/sum-body")
def calculate_sum_body(data: SumRequest):
    return {
        "a": data.a,
        "b": data.b,
        "result": data.a + data.b
    }