"""
appserver.py
- creates an application instance and runs the dev server
"""

from flask import render_template
from pyaepi.application import create_app
app = create_app()

# Create a URL route in our application for "/"
@app.route('/')
def home():
    """
    This function just responds to the browser ULR
    localhost:5000/

    :return: the rendered template 'home.html'
    """
    return render_template('home.html')


if __name__ == '__main__':
    app.run()

