"""
This is the main file for the Flask web application. It contains the routes and logic for the web application.

It has one page that displays a welcome message, when you visit the root URL of the web application.

"""
from flask import Flask, render_template

# Create a Flask application
app = Flask(__name__)

# Route for the root URL of the web application
# Create a page that displays a welcome message
# when you visit the root URL of the web application.
@app.route("/")
def docker_lab_welcome_page():
    """
    Create a page that displays a welcome message
    when you visit the root URL of the web application.
    """
    # Render the index.html template
    return render_template("index.html")
