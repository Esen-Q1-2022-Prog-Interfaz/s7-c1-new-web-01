from flask import Blueprint, render_template

site = Blueprint("site", __name__)


@site.route("/")
def home():
    return render_template("main/home.html")


@site.route("/about")
def about():
    return render_template("main/about.html")
