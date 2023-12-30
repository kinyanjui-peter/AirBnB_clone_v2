#!/usr/bin/env python3
"""script that starts a Flask web application:
    our web application must be listening on 0.0.0.0, port 5000
    Routes:
    /: display “Hello HBNB!”
    /hbnb: display “HBNB”
    You must use the option strict_slashes=False in your route definition
    """
from flask import Flask
#instance of Flask
app = Flask("__name__")

@app.route('/' , strict_slashes=False)
def func_to_display():
    """
    Routing to root, strict_slashes ensure
    the URL works when it ends both with or without the /
    """
    return "Hello HBNB!"


@app.route('/hbnb/' , strict_slashes=False)
def func_to_hbnb():
    """
    Routing to root, strict_slashes ensure
    the URL works when it ends both with or without the /
    """
    return "HBNB"
@app.route('/c/<text>', strict_slashes=False)
def func_to_c(text):
    """
    route to route and a text vallue added
    """
    return "C " + text



#prevent script from running if called#
if __name__ == "__main__":
    app.run("0.0.0.0", port=5000)
