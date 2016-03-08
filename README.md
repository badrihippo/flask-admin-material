# Flask Admin Material

This is actually a Material Design-themed admin interface to
[Flask-Admin](http://flask-admin.readthedocs.org/)
that I am developing for use in my own project. I thought it would be
useful to make it a separate repo so that it can be used in other projects,
too. The theme uses
[Material Design for Bootstrap](http://fezvrasta.github.io/bootstrap-material-design/)
to modify the native flask-admin `bootstrap3` templates

**Note: This interface is still work-in-progress. So feel free to use it,
but don't be surprised if drastic changes are suddenly introduced into the
interface!**

## Setup

After setting up your Flask app, import the helper `setup_templates` function
from flask-admin-material to initialize the templates in the app:

    from flask import Flask
    from flask_admin_material import setup_templates

    # Normal procedure for setting up Flask app
    app = Flask(__name__)

    # Run the setup_templates function
    app = setup_templates(app)
    
Also, when setting up Flask-Admin, select the `bootstrap3` template,
like so:

    admin = Admin(app, template_mode='bootstrap3')

If all goes well, your Flask-Admin interface will now be using a brand-new
Material Design theme!
