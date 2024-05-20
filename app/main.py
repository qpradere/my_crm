from fastapi import FastAPI
from api.api_v1.endpoints import accounts, contacts, users, leads

app = FastAPI()

# Include your routers
app.include_router(accounts.router, prefix="/accounts", tags=["accounts"])
app.include_router(contacts.router, prefix="/contacts", tags=["contacts"])
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(leads.router, prefix="/leads", tags=["leads"])

@app.get("/")
def read_root():
    return {"Hello": "World"}
