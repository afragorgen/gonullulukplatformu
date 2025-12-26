from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from extensions import db
from models.user import User
from utils.mail import send_email

auth_bp = Blueprint("auth", __name__)
@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        if User.query.filter_by(email=email).first():
            flash("Bu email zaten kayıtlı", "warning")
            return redirect(url_for("auth.register"))

        new_user = User(username=username, email=email)
        new_user.set_password(password)

        db.session.add(new_user)
        db.session.commit()

        # 📩 GERÇEK MAIL
        send_email(
            to=email,
            subject="Gönüllülük Platformu - Kayıt Başarılı",
            body=f"""
Merhaba {username},

Gönüllülük Platformu'na başarıyla kayıt oldun 🎉

İyi gönüllülükler dileriz 💚
"""
        )

        flash("Kayıt başarılı! Mail gönderildi.", "success")
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


@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Çıkış yapıldı", "success")
    return redirect(url_for("auth.login"))
