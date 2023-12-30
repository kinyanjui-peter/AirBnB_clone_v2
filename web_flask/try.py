from flask import Flask
import re

# instance of Flask
app = Flask(__name__)

# default values
def_text = "is cool"

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

                                        @app.route('/c/<text>', strict_slashes=False)
                                        def func_to_c(text):
                                                """
                                                    route to route and a text value added
                                                        """
                                                            underscore_text = re.sub(r'_', ' ', text)
                                                                """
                                                                    replace underscore with a space
                                                                        """
                                                                            return f"C {underscore_text}"

                                                                        @app.route('/python/<text>', strict_slashes=False)
                                                                        def display_python(text):
                                                                                """function that displays python"""
                                                                                    underscore_text = re.sub(r'_', ' ', text)
                                                                                        return f"Python {underscore_text}"

                                                                                    # prevent script from running if called
                                                                                    if __name__ == "__main__":
                                                                                            app.run("0.0.0.0", port=5000)

