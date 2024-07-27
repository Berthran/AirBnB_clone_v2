from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create an engine
engine = create_engine('mysql+mysqlconnector://hbnb_dev:hbnb_dev_pwd@localhost/hbnb_dev_db')

# Create a declarative base class
Base = declarative_base()

# Define a User class mapped to a users table
class User(Base):
    __tablename__ = 'user_table'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)

    def __repr__(self):
        return f"<User(name='{self.name}', email='{self.email}')>"

# Create the users table in the database
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Add a new user to the database
new_user = User(name='John Doe', email='john.doe@example.com')
session.add(new_user)
session.commit()

# Query the database
users = session.query(User).all()
for user in users:
    print(user)

