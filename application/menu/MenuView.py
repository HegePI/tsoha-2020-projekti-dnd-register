from application import app, db
from flask import Flask, flash, redirect, render_template, request, url_for
from flask_login import current_user
from application.user.UserModel import User
from application.adventure.AdventureModel import Adventure
from flask_login import login_required


@app.route("/menu")
@login_required
def main_menu():
    return render_template("menu/menu.html",
    users_adventures=Adventure.find_users_ongoing_adventures(current_user.id),
    all_adventures=Adventure.find_all_adventures(current_user.id))
