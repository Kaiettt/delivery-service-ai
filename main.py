from fastapi import FastAPI

from views.router import router

app = FastAPI(title="Delivery API", version="1.0")

app.include_router(router)

@app.get("/")
def home():
    return {"message": "Welcome to the Delivery Service API"}
