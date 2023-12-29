#!/usr/bin/python3
""" A script that starts Flask web application
    Your web application must be listening on 0.0.0.0, port 5000
    Routes:
    /: display “Hello HBNB!”
    You must use the option strict_slashes=False in your route definition
    """
from flask import Flask

app = Flask("__main__")
""" Flask class object"""

@app.route('/display' , strict_slashes=False)

def funct_to_display():
    """function that displays Hello HBNB!"""
    return "Hello HBNB!"

#prevent the script from running when called#
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
