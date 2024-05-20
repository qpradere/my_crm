from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
import uuid

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    contacts = relationship("Contact", back_populates="owner")

class Account(Base):
    __tablename__ = 'accounts'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    name = Column(String, index=True)
    industry = Column(String)
    phone = Column(String)
    website = Column(String)
    employees = Column(Integer)
    notes = Column(String)
    hq_city = Column(String)
    hq_state = Column(String)
    hq_country = Column(String)

    contacts = relationship("Contact", back_populates="account")

class Contact(Base):
    __tablename__ = 'contacts'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    email = Column(String, index=True)
    phone = Column(String)
    title = Column(String)
    notes = Column(String)
    city = Column(String)
    state = Column(String)
    country = Column(String)
    account_id = Column(UUID(as_uuid=True), ForeignKey('accounts.id'))

    account = relationship("Account", back_populates="contacts")
    owner = relationship("User", back_populates="contacts")

class Lead(Base):
    __tablename__ = 'leads'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    source = Column(String)
    status = Column(String)
    contact_id = Column(UUID(as_uuid=True), ForeignKey('contacts.id'))

    contact = relationship("Contact", back_populates="leads")
