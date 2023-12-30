#!/usr/bin/python3
"""script that starts a Flask web application:
    web application must be listening on 0.0.0.0, port 5000Routes:
    /: display “Hello HBNB!”
    /hbnb: display “HBNB”
    /c/<text>: display “C ”, followed by the value of the text variable
    (replace underscore _ symbols with a space )
    /python/<text>: display “Python ”, followed by the value of the text
    variable (replace underscore _ symbols with a space )
    The default value of text is “is cool”
    You must use the option strict_slashes=False in your route definition  
    """
from flask import Flask
import re
#instance of Flask
app = Flask(__name__)

#default values
def_text = "is cool"
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
    underscore_text = re.sub(r'_', ' ', text)
    """
    replace underscore wiith a space
    """ 
    return f"C {underscore_text}"

@app.route('/python/<text>', strict_slashes=False)
def display_python(text=def_text):
    """function that display python"""
    underscore_text = re.sub(r'_',' ', text)
    return f"Python {underscore_text}"

#prevent script from running if called#
if __name__ == "__main__":
    app.run("0.0.0.0", port=5000)
