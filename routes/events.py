from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from models.event import Event
from models.participation import Participation
from extensions import db

events_bp = Blueprint("events", __name__)

@events_bp.route("/events")
def list_events():
    events = Event.query.all()
    return render_template("events.html", events=events)

@events_bp.route("/events/<int:event_id>")
def event_detail(event_id):
    event = Event.query.get_or_404(event_id)
    return render_template("event_detail.html", event=event)

@events_bp.route("/events/<int:event_id>/join", methods=["GET"])
@login_required
def join_event(event_id):
    already = Participation.query.filter_by(
        user_id=current_user.id,
        event_id=event_id
    ).first()

    if already:
        flash("Zaten bu etkinliğe katıldınız", "warning")
    else:
        p = Participation(user_id=current_user.id, event_id=event_id)
        db.session.add(p)
        db.session.commit()
        flash("Etkinliğe katıldınız 🎉", "success")

    return redirect(url_for("events.event_detail", event_id=event_id))
