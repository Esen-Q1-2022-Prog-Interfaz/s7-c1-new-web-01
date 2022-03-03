from app import app
from database.db import db

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    # corriendo la aplicacion flask
    # a este archivo darle play
    app.run(debug=True)
