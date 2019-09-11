from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
      <!-- create your form here -->
        <form action="/" method="post">
            Rotate by:
            <input name="rot" type="text" value=0>
            <br><br>
            <textarea name="text" rows="4" cols="50"></textarea>
            <br><br>
            <input type="submit">
        </form>
    </body>
</html>
"""

@app.route("/", methods=['POST'])
def encrypt():
    rot=request.form['rot']
    text=request.form['text']
    encrypt=rotate_string(text,rot)
    
    return "<h1>"+ encrypt + "</h1>"

@app.route("/")
def index():
    return form

app.run()