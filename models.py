from pydantic import BaseModel
from typing import Optional

class Contact(BaseModel):
    id: Optional[int] = None
    first_name: str
    last_name: str
    account: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    title: Optional[str] = None
    notes: Optional[str] = None
    
