from application import app, db, bcrypt
from flask import Flask, flash, redirect, render_template, request, url_for
from flask_bcrypt import Bcrypt
from application.user.Models import User


@app.route("/newUser")
def new_user_form():
    return render_template("user/new.html")


@app.route("/newUser", methods=["POST"])
def create_new_user():
    username = request.form.get("username")
    password = request.form.get("password")

    user = User.query.filter_by(username=username).first()

    if user != None:
        error = "Käyttäjänimi on jo käytössä."
        return render_template("user/new.html", error=error)
    else:
        hashed_password = bcrypt.generate_password_hash(password, 10)
        user = User(username, hashed_password)
        db.session().add(user)
        db.session().commit()
        message = "käyttäjä luotiin onnistuneesti!"
        return render_template("login/login.html", message=message)