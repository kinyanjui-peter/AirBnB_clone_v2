#!/usr/bin/python3
#A script that starts Flask web application
from flask import Flask

app = Flask("__main__")

@app.route('/display' , strict_slashes=False)
def funct_to_display():
    return "Hello HBNB!"
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
