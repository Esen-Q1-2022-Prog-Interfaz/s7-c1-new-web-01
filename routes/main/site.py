from flask import Blueprint, render_template
from models.contact import Contact
from database.db import db

site = Blueprint("site", __name__)


@site.route("/")
def home():
    """newContact = Contact("maria", "maria@test.com", "123")
    db.session.add(newContact)
    db.session.commit()"""
    contactList = Contact.query.all()
    return render_template("main/home.html", contacts=contactList)


@site.route("/about")
def about():
    return render_template("main/about.html")
