from fastapi import APIRouter, HTTPException
from typing import List
from uuid import UUID, uuid4

import sys
from pathlib import Path

# Add the parent's parent directory to sys.path
current_dir = Path(__file__).resolve()
parent_parent_dir = current_dir.parent.parent
sys.path.append(str(parent_parent_dir))
from schemas import AccountCreate, AccountRead, AccountUpdate  # Adjust the import path as necessary

router = APIRouter()

# Mock database for demonstration purposes
accounts_db: List[AccountRead] = []  # Use AccountRead schema for mock DB entries

@router.get("/", response_model=List[AccountRead])
async def read_all_accounts():
    return accounts_db

@router.post("/", response_model=AccountRead, status_code=201)
async def create_account(account_create: AccountCreate):
    # Create a new AccountRead instance from AccountCreate data
    new_account = AccountRead(
        id=uuid4(),  # Generate a new UUID for the account
        **account_create.dict()  # Unpack account_create fields into the new AccountRead
    )
    accounts_db.append(new_account)
    return new_account

@router.get("/{account_id}", response_model=AccountRead)
async def read_account(account_id: UUID):
    for account in accounts_db:
        if account.id == account_id:
            return account
    raise HTTPException(status_code=404, detail="Account not found")

@router.put("/{account_id}", response_model=AccountRead)
async def update_account(account_id: UUID, account_update: AccountUpdate):
    for idx, account in enumerate(accounts_db):
        if account.id == account_id:
            # Create a dict of the current account, update with provided values, and unpack back into AccountRead
            updated_account_data = accounts_db[idx].dict()
            updated_fields = account_update.dict(exclude_unset=True)
            updated_account_data.update(updated_fields)
            accounts_db[idx] = AccountRead(**updated_account_data)
            return accounts_db[idx]
    raise HTTPException(status_code=404, detail="Account not found")

@router.delete("/{account_id}", status_code=204)
async def delete_account(account_id: UUID):
    for idx, account in enumerate(accounts_db):
        if account.id == account_id:
            del accounts_db[idx]
            return
    raise HTTPException(status_code=404, detail="Account not found")
