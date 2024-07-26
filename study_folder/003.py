# How to use environment variables in Python

import os

# Set environment variables
os.environ['DATABASE_USER'] = 'username'
os.environ['DATABASE_PASSWORD'] = 'password'

# Access environment variables
db_user = os.getenv('DATABASE_USER')
db_password = os.getenv('DATABASE_PASSWORD')

print(f"User: {db_user}")
print(f"Password: {db_password}")


# In a real application, you might store these in a .env file and use a library like python-dotenv to load them.

# .env file
# os.environ['DATABASE_USER'] = 'username'
# os.environ['DATABASE_PASSWORD'] = 'password'

# Install the library
# pip install python-dotenv

from dotenv import load_dotenv

load_dotenv()

db_user = os.getenv('DATABASE_USER')
db_password = os.getenv('DATABASE_PASSWORD')

print(f"User: {db_user}")
print(f"Password: {db_password}")

