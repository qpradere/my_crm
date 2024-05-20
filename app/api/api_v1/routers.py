from fastapi import APIRouter
from .endpoints import contacts, accounts, users, leads

api_router = APIRouter()
api_router.include_router(contacts.router, prefix="/contacts", tags=["contacts"])
api_router.include_router(accounts.router, prefix="/accounts", tags=["accounts"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(leads.router, prefix="/leads", tags=["leads"])
