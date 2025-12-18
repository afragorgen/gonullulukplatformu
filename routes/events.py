from flask import Blueprint, render_template, request, redirect, url_for, abort
from flask_login import current_user, login_required
from extensions import db
from models.event import Event

events_bp = Blueprint("events_bp", __name__)

# 📌 Etkinlikleri listele
@events_bp.route("/events")
def events():
    event_list = Event.query.all()
    return render_template("events.html", events=event_list)


# 📌 Etkinlik detay sayfası
@events_bp.route("/events/<int:event_id>")
def event_detail(event_id):
    event = Event.query.get_or_404(event_id)

    # Bu sayfa sadece detay gösterir
    # Kimler başvurmuş kısmını template'te kontrol edeceğiz
    return render_template("event_detail.html", event=event)


# 📌 Etkinlik oluştur
@events_bp.route("/events/create", methods=["GET", "POST"])
@login_required
def create_event():
    if request.method == "POST":
        title = request.form["title"]
        description = request.form["description"]
        date = request.form["date"]
        location = request.form["location"]

        new_event = Event(
            title=title,
            description=description,
            date=date,
            location=location,
            image_url="images/animal.jpg",  # şimdilik sabit
            created_by_id=current_user.id
        )

        db.session.add(new_event)
        db.session.commit()

        return redirect(url_for("events_bp.events"))

    return render_template("event_create.html")
