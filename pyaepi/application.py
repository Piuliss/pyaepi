"""
application.py
- creates a Flask app instance and registers the database object
"""

from flask import Flask


def create_app(app_name='PYAEPI'):
    app = Flask(app_name, template_folder="templates")
    app.config.from_object('pyaepi.config.BaseConfig')

    from pyaepi.api import api
    app.register_blueprint(api, url_prefix="/api")

    from pyaepi.models import db
    db.init_app(app)

    return app
