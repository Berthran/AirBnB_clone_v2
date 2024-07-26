## How to render HTML 

- Step 1: Create a `templates` directory
This directory will contain the html files to render
```sh
mkdir templates
```

- Step 2: import the `render_template` method
```py
from flask import render_template
```

- Step 3: create and write the HTML file to render
```sh
touch templates/number_template.html
```
```html
<!DOCTYPE html>
<HTML lang="en">
    <HEAD>
        <TITLE>HBNB</TITLE>
    </HEAD>
    <BODY>
        <H1>Number: 89</H1>
    </BODY>
</HTML>
```

- Step 4: render the html
```py
@app.route('\number_template\<int:n>')
def render_n(n):
	return render_template('number_template.html')
```
