from pydantic import BaseModel, Field
from typing import Optional, List
from uuid import UUID, uuid4

class ContactBase(BaseModel):
    first_name: str
    last_name: str
    email: Optional[str] = None
    phone: Optional[str] = None
    title: Optional[str] = None
    notes: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    country: Optional[str] = None

# Define Account model before referencing it in Contact
class AccountBase(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    industry: Optional[str] = None
    phone: Optional[str] = None
    website: Optional[str] = None
    employees: Optional[int] = None
    notes: Optional[str] = None
    hq_city: Optional[str] = None
    hq_state: Optional[str] = None
    hq_country: Optional[str] = None
    # Assuming contacts will be a list of ContactBase items
    contacts: List[ContactBase] = []

class Contact(ContactBase):
    id: UUID = Field(default_factory=uuid4)
    account_id: Optional[UUID] = None  

class Account(AccountBase):
    contacts: List[Contact] = []
