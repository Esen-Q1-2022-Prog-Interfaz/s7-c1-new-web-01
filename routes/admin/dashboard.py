from flask import Blueprint, render_template

dashboard = Blueprint("dashboard", __name__, url_prefix="/admin")


@dashboard.route("/")
def main():
    return render_template("admin/login.html")


@dashboard.route("/dashboard")
def dashboard():
    return render_template("admin/dashboard.html")
