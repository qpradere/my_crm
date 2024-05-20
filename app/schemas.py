from pydantic import BaseModel, EmailStr
from typing import Optional, List
from uuid import UUID

# Contact Schemas
class ContactBase(BaseModel):
    first_name: str
    last_name: str
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    title: Optional[str] = None
    notes: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    country: Optional[str] = None

class ContactCreate(ContactBase):
    account_id: UUID

class ContactRead(ContactBase):
    id: UUID
    account_id: Optional[UUID] = None

    class Config:
        from_attributes = True  # Updated for Pydantic v2

class ContactUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    title: Optional[str] = None
    notes: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    country: Optional[str] = None
    account_id: Optional[UUID] = None

# Account Schemas
class AccountBase(BaseModel):
    name: str
    industry: Optional[str] = None
    phone: Optional[str] = None
    website: Optional[str] = None
    employees: Optional[int] = None
    notes: Optional[str] = None
    hq_city: Optional[str] = None
    hq_state: Optional[str] = None
    hq_country: Optional[str] = None

class AccountCreate(AccountBase):
    pass

class AccountRead(AccountBase):
    id: UUID
    contacts: List[ContactRead] = []

    class Config:
        from_attributes = True  # Updated for Pydantic v2

class AccountUpdate(BaseModel):
    name: Optional[str] = None
    industry: Optional[str] = None
    phone: Optional[str] = None
    website: Optional[str] = None
    employees: Optional[int] = None
    notes: Optional[str] = None
    hq_city: Optional[str] = None
    hq_state: Optional[str] = None
    hq_country: Optional[str] = None

# User Schemas
class UserBase(BaseModel):
    first_name: str
    last_name: str
    username: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserRead(UserBase):
    id: UUID
    is_active: bool

    class Config:
        from_attributes = True  # Updated for Pydantic v2

class UserUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    is_active: Optional[bool] = None

# Lead Schemas
class LeadBase(BaseModel):
    source: str
    status: str

class LeadCreate(LeadBase):
    contact_id: UUID

class LeadRead(LeadBase):
    id: UUID
    contact_id: UUID

    class Config:
        from_attributes = True  # Updated for Pydantic v2

class LeadUpdate(BaseModel):
    source: Optional[str] = None
    status: Optional[str] = None
    contact_id: Optional[UUID] = None
