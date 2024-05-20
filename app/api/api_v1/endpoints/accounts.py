from fastapi import APIRouter, HTTPException, Depends
from typing import List
from sqlalchemy.orm import Session
from uuid import UUID

from models import Account
from schemas import AccountCreate, AccountRead, AccountUpdate
from database import get_db

router = APIRouter()

@router.get("/", response_model=List[AccountRead])
async def read_all_accounts(db: Session = Depends(get_db)):
    accounts = db.query(Account).all()
    return accounts

@router.post("/", response_model=AccountRead, status_code=201)
async def create_account(account: AccountCreate, db: Session = Depends(get_db)):
    db_account = Account(**account.model_dump()) 
    db.add(db_account)
    db.commit()
    db.refresh(db_account)
    return db_account

@router.get("/{account_id}", response_model=AccountRead)
async def read_account(account_id: UUID, db: Session = Depends(get_db)):
    account = db.query(Account).filter(Account.id == account_id).first()
    if not account:
        raise HTTPException(status_code=404, detail="Account not found")
    return account

@router.put("/{account_id}", response_model=AccountRead)
async def update_account(account_id: UUID, account: AccountUpdate, db: Session = Depends(get_db)):
    db_account = db.query(Account).filter(Account.id == account_id).first()
    if not db_account:
        raise HTTPException(status_code=404, detail="Account not found")
    for key, value in account.model_dump(exclude_unset=True).items():
        setattr(db_account, key, value)
    db.commit()
    db.refresh(db_account)
    return db_account

@router.delete("/{account_id}", status_code=204)
async def delete_account(account_id: UUID, db: Session = Depends(get_db)):
    account = db.query(Account).filter(Account.id == account_id).first()
    if not account:
        raise HTTPException(status_code=404, detail="Account not found")
    db.delete(account)
    db.commit()
