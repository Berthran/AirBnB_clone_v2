## The SQLAlchemy Object Relational Mapper

This ORM tool presents a way to associate:
- user-defined `Python classes` with `database tables` 
- and `instances` of those classes with `rows` in their corresponding tables.

## How to map Python Classes to MySQL Tables
- Step 1: Create connection
```py
>>> from sqlalchemy import create_engine
>>> engine = create_engine('sqlite:///:memory:', echo=True)
```

- Step 2: Declare a Mapping
In modern SQLAlchemy, a system know as `Declarative` can be used to create classes that include directives to describe the actual databse table they will be mapped to. Classes mapped using the Declarative system are defined in terms of a base class which maintains a catalog of classes and tables relative to that base - this is known as the declarative base class. We create the base class using the declarative_base() function, as follows:
```py
>>> from sqlalchemy.ext.declarative import declarative_base

>>> Base = declarative_base()
```
 We will start with just a single table called users, which will store records for the end-users using our application. A new class called User will be the class to which we map this table. Within the class, we define details about the table to which we’ll be mapping, primarily the table name, and names and datatypes of columns:
```py
>>> from sqlalchemy import Column, Integer, String
>>> class User(Base):
...     __tablename__ = 'users'
...
...     id = Column(Integer, primary_key=True)
...     name = Column(String)
...     fullname = Column(String)
...     nickname = Column(String)
...
...     def __repr__(self):
...        return "<User(name='%s', fullname='%s', nickname='%s')>" % (
...                             self.name, self.fullname, self.nickname)
```