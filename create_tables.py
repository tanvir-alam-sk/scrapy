from sqlalchemy import create_engine
from models import Base

# Connect to the database
engine = create_engine('postgresql://your_username:your_password@localhost:5432/your_database')

# Create all tables from models
Base.metadata.create_all(engine)

print("Tables created successfully!")

