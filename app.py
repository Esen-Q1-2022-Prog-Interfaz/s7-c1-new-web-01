from flask import Flask
from routes.main.site import site
from routes.admin.dashboard import dashboard

# creando una instancia
app = Flask(__name__)

app.register_blueprint(site)
app.register_blueprint(dashboard)
