from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List
from uuid import UUID

# Base schema for creating a new contact, similar to ContactBase but for input
class ContactCreate(BaseModel):
    first_name: str
    last_name: str
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    title: Optional[str] = None
    notes: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    country: Optional[str] = None

# Schema for reading a contact, including ID and account_id
class ContactRead(BaseModel):
    id: UUID
    first_name: str
    last_name: str
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    account_id: Optional[UUID] = None
    class Config:
        orm_mode = True

# Similar approach for Account
class AccountCreate(BaseModel):
    name: str
    industry: Optional[str] = None
    phone: Optional[str] = None
    website: Optional[str] = None
    employees: Optional[int] = None
    notes: Optional[str] = None
    hq_city: Optional[str] = None
    hq_state: Optional[str] = None
    hq_country: Optional[str] = None

class AccountRead(BaseModel):
    id: UUID
    name: str
    industry: Optional[str] = None
    phone: Optional[str] = None
    website: Optional[str] = None
    employees: Optional[int] = None
    notes: Optional[str] = None
    hq_city: Optional[str] = None
    hq_state: Optional[str] = None
    hq_country: Optional[str] = None
    contacts: List[ContactRead] = []  # Assuming you want to include contacts here
    class Config:
        orm_mode = True
