## Understanding the components of the `create_engine` method
```py
from sqlalchemy import create_engine
engine = create_engine('postgresql://scott:tiger@localhost:5432/mydatabase')
```

The above code does the following:
- Creates a `Dialect` object tailored towards PostgreSQL
- Creates a `Pool` object which will
- Establish a `DBAPI connection` at `localhost:5432`



## When does an engine establish connection to the database
Note that the Engine and its underlying Pool do not establish the first actual DBAPI connection until the Engine.connect() method is called, or an operation which is dependent on this method such as Engine.execute() is invoked. In this way, Engine and Pool can be said to have a lazy initialization behavior.

## The typical form of a database URL is:
```py
dialect+driver://username:password@host:port/database
```
Examples of SQLAlchemy dialects are `sqlite, mysql, postgresql, oracle, or mssql`.
The drivername is the name of the DBAPI to be used to connect to the database using all lowercase letters. If not specified, a “default” DBAPI will be imported if available - this default is typically the most widely known driver available for that backend.


### MySQL dialect
The MySQL dialect uses mysql-python as the default DBAPI. There are many MySQL DBAPIs available, including MySQL-connector-python and OurSQL:
```py
# default
engine = create_engine('mysql://scott:tiger@localhost/foo')

# mysqlclient (a maintained fork of MySQL-Python)
engine = create_engine('mysql+mysqldb://scott:tiger@localhost/foo')

# PyMySQL
engine = create_engine('mysql+pymysql://scott:tiger@localhost/foo')
```

