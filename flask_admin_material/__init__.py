__author__ = 'Badri Sunderarajan'
__email__ = 'badrihippo@gmail.com'

from flask import Blueprint
from flask.helpers import get_root_path
import jinja2
import os

def setup_templates(app):
    '''
    Takes in a Flask app and sets up the templates and staticfiles from
    this project (via jinja2 loader and blueprint).

    Thanks to https://github.com/lex009/flask-admin-lte for inspiration
    '''
    extra_template_path = os.path.join(get_root_path('flask_admin_material'), 'templates')
    my_loader = jinja2.ChoiceLoader([
            app.jinja_loader,
            jinja2.FileSystemLoader(extra_template_path),
        ])
    app.jinja_loader = my_loader
    app.register_blueprint(Blueprint('admin_theme', __name__, static_folder='static', static_url_path='/static/admin_theme'))
    return app
