from fastapi import FastAPI
from models import Contact
from typing import List

app = FastAPI()

# Mock database
contacts_db = []

@app.get("/")
async def root():
    return {"message": "Hello World"}

##Crud Operations

# Create a New Contact
@app.post("/contacts/", response_model=Contact)
async def create_contact(contact: Contact):
    contact.id = len(contacts_db) + 1
    contacts_db.append(contact)
    return contact

# Read a Contact by ID
@app.get("/contacts/{contact_id}", response_model=Contact)
async def read_contact(contact_id: int):
    for contact in contacts_db:
        if contact.id == contact_id:
            return contact
    return {"message": "Contact not found"}

# Update a Contact by ID
@app.put("/contacts/{contact_id}", response_model=Contact)
async def update_contact(contact_id: int, updated_contact: Contact):
    for idx, contact in enumerate(contacts_db):
        if contact.id == contact_id:
            contacts_db[idx] = updated_contact
            return updated_contact
    return {"message": "Contact not found"}

# Delete a Contact by ID
@app.delete("/contacts/{contact_id}")
async def delete_contact(contact_id: int):
    for idx, contact in enumerate(contacts_db):
        if contact.id == contact_id:
            del contacts_db[idx]
            return {"message": "Contact deleted"}
    return {"message": "Contact not found"}
