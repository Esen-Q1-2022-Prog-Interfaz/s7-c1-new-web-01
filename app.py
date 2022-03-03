from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from routes.main.site import site
from routes.admin.dashboard import dashboard

# creando una instancia
app = Flask(__name__)

# loading configuration for
# flask app
# sqlalchemy
app.config.from_object("config.BaseConfig")


app.register_blueprint(site)
app.register_blueprint(dashboard)

SQLAlchemy(app)
