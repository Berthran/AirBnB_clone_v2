## How to run Flask app

1. Using `flask` app
- Set the `FLASK_APP` env variable
```sh
export FLASH_APP=flask_blog.py
```
*Pro*: allows debugging with the Flask shell
*Con*: requires restarting the server to view changes
- (Optional) Set the `FLASK_ENV` env variable to run in debug mode
```sh
export FLASK_DEBUG=1
```
Pro: changes are implemented without restarting the server
- Run the command
```sh
flask run
```
This runs the app in the flask server at a given IP address

2. Using `python3`
- Set a conditional for the `__name__` attribute in the flask script
```py
if __name__ == '__main__':
	app.run(debug=True)
```
- Run the command
```sh
python3 flask_blog.py
```

