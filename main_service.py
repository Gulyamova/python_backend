from fastapi import FastAPI
from pydantic import BaseModel
import requests
import time
import uvicorn

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str


ORDER_SERVICE_URL = "http://localhost:8001"
AUTH_SERVICE_URL = "http://localhost:8002"


@app.post("/create_order/")
async def create_order(item: Item):
    # обращаемся к сервису обработки заказов и аутентификации
    auth_response = requests.post(f"{AUTH_SERVICE_URL}/authenticate/")
    if auth_response.status_code != 200:
        return {"error": "Authentication failed"}

    order_response = requests.get(f"{ORDER_SERVICE_URL}/process_order/1")
    if order_response.status_code != 200:
        return {"error": "Order processing failed"}

    # Имитация создания заказа с задержкой
    time.sleep(2)
    return {"message": "Order created", "item": item}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
