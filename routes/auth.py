from flask import Blueprint, render_template, request, redirect, url_for, flash
from extensions import db
from models.user import User
from flask_login import login_user, logout_user, login_required, current_user

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        existing_user = User.query.filter(
            (User.username == username) | (User.email == email)
        ).first()

        if existing_user:
            flash("Bu kullanıcı adı veya email zaten kayıtlı", "danger")
            return redirect(url_for("auth.register"))

        user = User(username=username, email=email)
        user.set_password(password)

        db.session.add(user)
        db.session.commit()

        flash("Kayıt başarılı! Giriş yapabilirsiniz.", "success")
        return redirect(url_for("auth.login"))

    return render_template("register.html")


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        user = User.query.filter_by(email=email).first()

        if user and user.check_password(password):
            login_user(user)
            flash("Giriş başarılı", "success")
            return redirect(url_for("main.home"))

        flash("Email veya şifre hatalı", "danger")
        return render_template("login.html") 

    return render_template("login.html")



@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Çıkış yapıldı", "info")
    return redirect(url_for("main.home"))
