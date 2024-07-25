## How to handle Variables in a route

### Add variable sections to a URL
1. Using a variable name enclosed in '<>'
```py
@app.route('/user/<username>')
```
2. Using a converter to specify the type of the variable
```py
@app.route('/post/<int:post_id>')
```

**What hapeens when a variable is used in the URL section of the route decorator?**

The function receives the `variable_name` as a keyword argument.
```py
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'
```