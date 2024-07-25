## How to define a Flask route

- Use the `@app.route` decorator
Routes are used to bind URL patterns to functions
The forward slash '/' represents the home page of the app
```py
@app.route('/')
```
- Create a function to perform action
```py
def homepage():
    return '<h1> HomePage </h1>'
```

**Full route**
```py
@app.route('/')
def homepage():
    return '<h1> HomePage </h1>'
```

**More examples**
```py
@app.route('/about')
def about():
    return '<h1> About Page </h1>'
```

**Tie multiple routes to same action**
```py
@app.route('/')
@app.route('/home')
def homepage():
    return '<h1> HomePage </h1>'
```
