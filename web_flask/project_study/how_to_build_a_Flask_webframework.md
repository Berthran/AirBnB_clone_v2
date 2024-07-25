## Import Flask
```py
from flask import Flask
```

## Create an instance of the Flask class
```py
app = Flask(__name__)
```

## Define a route or routes
```py
@app.route('/')
def home():
    return <h1>Home Page </h1>
```
