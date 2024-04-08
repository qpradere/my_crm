from fastapi import FastAPI
# Import routers
from app.routers import contact_router, account_router

app = FastAPI(title="CRM API", version="1.0")

# Include routers in the application
app.include_router(
    contact_router.router,
    prefix="/contacts",
    tags=["contacts"]
)
app.include_router(
    account_router.router,
    prefix="/accounts",
    tags=["accounts"]
)

@app.get("/")
async def root():
    return {"message": "Welcome to the CRM API!"}
