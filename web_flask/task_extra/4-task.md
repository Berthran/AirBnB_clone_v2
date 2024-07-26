## How to use a converted to specify the type of argument passed to a URL

```py
@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'
```
This ensures that only integer numbers are valid.