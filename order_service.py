from fastapi import FastAPI
import time

app = FastAPI()


@app.get("/process_order/{order_id}")
async def process_order(order_id: int):
    # Имитация обработки заказа с задержкой
    time.sleep(3)
    return {"message": f"Order {order_id} processed"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
