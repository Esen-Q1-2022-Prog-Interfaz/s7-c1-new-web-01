from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy
from routes.main.site import site
from routes.admin.dashboard import dashboard

# creando una instancia
app = Flask(__name__)

app.config.from_object("config.BaseConfig")
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:root@localhost:3306/todolistdb"


app.register_blueprint(site)
app.register_blueprint(dashboard)

SQLAlchemy(app)
