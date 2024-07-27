#!/usr/bin/python3
"""This module defines a class to manage databased storage for hbnb clone"""
import os
import json
from sqlalchemy import create_engine, text, inspect
from sqlalchemy.orm import sessionmaker

class DBStorage:
    """This class manages storage of hbnb models using MySQL database"""
    __engine = None
    __session = None

    def __init__(self):
        """Setup an instance of the class"""
        # Retriev environment variables
        db_user = os.getenv('HBNB_MYSQL_USER')
        db_pwd = os.getenv('HBNB_MYSQL_PWD')
        db_host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')
        db_env = os.getenv('HBNB_ENV')

        print(db_user, db_pwd, db_host, db, db_env)
        
        # Create database engine
        self.__engine = create_engine(f'mysql+mysqldb://{db_user}:{db_pwd}@{db_host}/{db}', pool_pre_ping=True)

        # Create session for querying database
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()

        # Remove tables if in "test" environment
        if db_env == 'test':
            inspector = inspect(self.__engine)
            table_names = inspector.get_table_names()
            for table in table_names:
                drop_query = text(f"DROP TABLE IF EXISTS {table}")
                print(f"Dropping table {table}")
                self.__session.execute(drop_query)

    def all(self, cls=None):
        dictionary = {}
        pass
