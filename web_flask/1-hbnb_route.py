#!/usr/bin/python3
"""script that starts a Flask web application:
    our web application must be listening on 0.0.0.0, port 5000
    Routes:
    /: display “Hello HBNB!”
    /hbnb: display “HBNB”
    You must use the option strict_slashes=False in your route definition
    code
    """
from flask import Flask


# instance of Flask
app = Flask("__main__")


@app.route('/', strict_slashes=False)
def func_to_display():
    """
    Routing to root, strict_slashes ensure
    the URL works when it ends both with or without the /
    """
    return "Hello HBNB!"


@app.route('/hbnb/', strict_slashes=False)
def func_to_hbnb():
    """
    Routing to root, strict_slashes ensure
    the URL works when it ends both with or without the /
     """
    return "HBNB"


# prevent script from running if called#
if __name__ == "__main__":
    app.run("0.0.0.0", port=5000)
