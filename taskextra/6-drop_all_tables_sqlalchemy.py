from sqlalchemy import create_engine, text, inspect

# Create an engine. Replace 'username', 'password', 'hostname', and 'database_name' with your actual database credentials
engine = create_engine('mysql+mysqlconnector://username:password@hostname/database_name')

# Connect to the database
with engine.connect() as connection:
    # Get the inspector object
    inspector = inspect(engine)
    
    # Get the list of all table names
    table_names = inspector.get_table_names()
    
    # Drop all tables
    for table_name in table_names:
        drop_table_query = text(f"DROP TABLE IF EXISTS {table_name}")
        connection.execute(drop_table_query)
        print(f"Table '{table_name}' dropped successfully.")

