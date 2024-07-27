from sqlalchemy import create_engine, text, inspect
from sqlalchemy.orm import sessionmaker

# Create an engine. Replace 'username', 'password', 'hostname', and 'database_name' with your actual database credentials
engine = create_engine('mysql+mysqlconnector://username:password@hostname/database_name')

# Create a sessionmaker bound to the engine
Session = sessionmaker(bind=engine)

# Create a new session
with Session() as session:
    # Get the inspector object
    inspector = inspect(engine)
    
    # Get the list of all table names
    table_names = inspector.get_table_names()
    
    # Drop all tables
    for table_name in table_names:
        drop_table_query = text(f"DROP TABLE IF EXISTS {table_name}")
        session.execute(drop_table_query)
        print(f"Table '{table_name}' dropped successfully.")

