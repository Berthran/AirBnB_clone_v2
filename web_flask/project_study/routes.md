### What is a route
A route is a **URL pattern** associated with a **specific function** that handles the **logic** for that URL endpoint. 

### Why purpose do routes serves
Basically, routes determine how URLs are processed and what content is returned to the client.

### The `route()` decorator
The `route()` decorator is used to bind a function to a URL.

### How to define a route in Flask
```py
# Route decorator with the URL in brackets
@app.route('/') 
# Function handling logic for URL endpoint
def function_name(arg): 
    return "Content to show client"
```

