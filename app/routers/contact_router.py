from fastapi import APIRouter, HTTPException
from typing import List
from uuid import UUID, uuid4

import sys
from pathlib import Path

# Add the parent's parent directory to sys.path
current_dir = Path(__file__).resolve()
parent_parent_dir = current_dir.parent.parent
sys.path.append(str(parent_parent_dir))
from schemas import ContactCreate, ContactRead, ContactUpdate  # Assuming schemas.py is correctly placed

# Initialize API router
router = APIRouter()

# Mock database for demonstration purposes
contacts_db: List[ContactRead] = []
accounts_db_ids = [uuid4()]  # Example list of account UUIDs for validation

@router.get("/", response_model=List[ContactRead])
async def read_all_contacts():
    return contacts_db

@router.post("/", response_model=ContactRead, status_code=201)
async def create_contact(contact_create: ContactCreate):
    # Validate account_id exists
    if contact_create.account_id not in accounts_db_ids:
        raise HTTPException(status_code=400, detail="Account not found")

    # Create and save the new contact
    new_contact = ContactRead(
        id=uuid4(),  # Assign a unique UUID
        **contact_create.dict()  # Unpack contact_create fields into the new ContactRead
    )
    contacts_db.append(new_contact)
    return new_contact

@router.get("/{contact_id}", response_model=ContactRead)
async def read_contact(contact_id: UUID):
    for contact in contacts_db:
        if contact.id == contact_id:
            return contact
    raise HTTPException(status_code=404, detail="Contact not found")

@router.put("/{contact_id}", response_model=ContactRead)
async def update_contact(contact_id: UUID, updated_contact: ContactUpdate):
    for idx, contact in enumerate(contacts_db):
        if contact.id == contact_id:
            # Create a new instance of ContactRead with updated values
            updated_data = contact.dict()
            updated_fields = updated_contact.dict(exclude_unset=True)
            updated_data.update(updated_fields)
            updated_data["id"] = contact_id  # Ensure the ID remains unchanged
            contacts_db[idx] = ContactRead(**updated_data)
            return contacts_db[idx]
    raise HTTPException(status_code=404, detail="Contact not found")

@router.delete("/{contact_id}", status_code=204)
async def delete_contact(contact_id: UUID):
    for idx, contact in enumerate(contacts_db):
        if contact.id == contact_id:
            del contacts_db[idx]
            return
    raise HTTPException(status_code=404, detail="Contact not found")
