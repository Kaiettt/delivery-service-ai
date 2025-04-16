from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  # ✅ import CORS middleware
from views.router import router

app = FastAPI(title="Delivery API", version="1.0")

# ✅ Add CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # ✅ React frontend origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Include your API router
app.include_router(router)

@app.get("/")
def home():
    return {"message": "Welcome to the Delivery Service API"}
