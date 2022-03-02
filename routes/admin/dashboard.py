from flask import Blueprint

dashboard = Blueprint("dashboard", __name__, url_prefix="/admin")


@dashboard.route("/")
def main():
    return "admin main pagez"


@dashboard.route("/product")
def product():
    return "admin product pagez"
