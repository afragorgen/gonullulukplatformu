from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash

from extensions import db
from models.user import User

auth_bp = Blueprint("auth_bp", __name__)


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        # Aynı kullanıcı var mı kontrolü
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash("Bu email zaten kayıtlı", "danger")
            return redirect(url_for("auth_bp.register"))

        new_user = User(
            username=username,
            email=email,
            password_hash=generate_password_hash(password),
            role="user"
        )

        db.session.add(new_user)
        db.session.commit()

        flash("Kayıt başarılı, giriş yapabilirsiniz", "success")
        return redirect(url_for("auth_bp.login"))

    return render_template("register.html")


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password_hash, password):
            session["user_id"] = user.id
            session["username"] = user.username
            flash("Giriş başarılı", "success")
            return redirect(url_for("main.home"))

        flash("Email veya şifre hatalı", "danger")
        return redirect(url_for("auth_bp.login"))

    return render_template("login.html")


@auth_bp.route("/logout")
def logout():
    session.clear()
    flash("Çıkış yapıldı", "info")
    return redirect(url_for("main.home"))
