from fastapi import FastAPI
import time

app = FastAPI()


@app.post("/authenticate/")
async def authenticate_user():
    # Имитация аутентификации пользователя с задержкой
    time.sleep(1)
    return {"message": "User authenticated"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8002)
