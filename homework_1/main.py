from fastapi import FastAPI, Path, Query
from pydantic import BaseModel

app = FastAPI()


class GreetingRequest(BaseModel):
    name: str


@app.get("/hello/{name}")
async def hello_name(name: str = Path(..., description="Name of the person")):
    """
    Say hello to a person with a given name.

    - **name**: Name of the person in the path.
    """
    return {"message": f"Hello, {name}!"}


@app.get("/greet")
async def greet_name(name: str = Query(..., description="Name of the person")):
    """
    Greet a person with a given name.

    - **name**: Name of the person in the query parameter.
    """
    return {"message": f"Greetings, {name}!"}


@app.post("/greeting")
async def create_greeting(request: GreetingRequest):
    """
    Create a custom greeting for a person.

    - **request**: Request body containing the person's name.
    """
    return {"message": f"Custom greeting, {request.name}!"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
