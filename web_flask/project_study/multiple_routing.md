Yes, it is possible to achieve this in a single route definition using the `werkzeug.routing.Rule` class, but within the confines of Flask's built-in `route` decorator, achieving it in a single line directly isn't possible due to the need to handle multiple routes. However, there is a slightly more compact way to define your route using `defaults` and handling multiple rules in a single `@app.route` decorator with a common function:

Here's the streamlined way to achieve it:

```python
from flask import Flask

app = Flask(__name__)

@app.route('/python/', defaults={'variable': 'is cool'}, strict_slashes=False)
@app.route('/python/<variable>', strict_slashes=False)
def python_variable(variable):
    return f'Python {variable}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
```

### Explanation

1. **First `@app.route()`**: 
   - Handles both `/python` and `/python/` due to `strict_slashes=False` and sets the default `variable` to `"is cool"`.
2. **Second `@app.route()`**:
   - Handles `/python/<variable>` where `<variable>` can be any custom value.

### Testing

- Accessing `/python` or `/python/` will return `Python is cool`.
- Accessing `/python/<any_value>` will return `Python <any_value>`.

While this still uses two `@app.route()` decorators, it reduces redundancy and ensures the routes are concise and easily understandable. Combining routes like this in one function is as close as you can get to a single-line solution while maintaining readability and functionality within Flask's routing capabilities.
