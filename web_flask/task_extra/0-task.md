## `app.run()` Method

Specifying the host and port to run the web application

**Function Prototype**:
```py
app.run(host=None, port=None, debug=None, load_dotenv=True, **options)
```

Runs the application on a local development server.

**Note**: Do not use `app.run()` in a production setting. It is not intended to meet security and performance requirements for a production server. For production, see [Deploying to Production](https://flask.palletsprojects.com/en/latest/deploying/) for WSGI server recommendations.

### Debug Mode

- If the `debug` flag is set, the server will automatically reload for code changes and show a debugger in case an exception occurs.
- To run the application in debug mode but disable code execution on the interactive debugger, pass `use_evalex=False` as a parameter. This keeps the debugger’s traceback screen active but disables code execution.

**Note**: It is not recommended to use this function for development with automatic reloading as this is poorly supported. Instead, use the Flask command-line script’s run support.

### Keep in Mind

- Flask will suppress any server error with a generic error page unless it is in debug mode. To enable just the interactive debugger without code reloading, invoke `app.run()` with `debug=True` and `use_reloader=False`. Setting `use_debugger` to `True` without being in debug mode won’t catch any exceptions because there won’t be any to catch.

### Parameters

- `host` (`str | None`): The hostname to listen on. Set this to `'0.0.0.0'` to make the server available externally. Defaults to `'127.0.0.1'` or the host in the `SERVER_NAME` config variable if present.
- `port` (`int | None`): The port of the web server. Defaults to `5000` or the port defined in the `SERVER_NAME` config variable if present.
- `debug` (`bool | None`): If given, enable or disable debug mode.
- `load_dotenv` (`bool`): Load the nearest `.env` and `.flaskenv` files to set environment variables. Also changes the working directory to the directory containing the first file found.
- `options` (`Any`): Options to be forwarded to the underlying Werkzeug server. See `werkzeug.serving.run_simple()` for more information.

### Return Type

- `None`