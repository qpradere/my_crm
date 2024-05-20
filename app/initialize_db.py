# initialize_db.py
from sqlalchemy.orm import sessionmaker
from models import Base  # Import your models
from database import engine  # Import the engine from your database setup

# Create all tables in the database
Base.metadata.create_all(bind=engine)
