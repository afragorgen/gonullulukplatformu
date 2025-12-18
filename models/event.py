from datetime import datetime
from extensions import db
from models.participation import participation

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=False)
    date = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(120), nullable=False)
    image_url = db.Column(db.String(300))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    volunteers = db.relationship(
        "User",
        secondary=participation,
        backref=db.backref("joined_events", lazy="dynamic")
    )
    created_by_id = db.Column(
    db.Integer,
    db.ForeignKey("user.id"),
    nullable=False
)
created_by = db.relationship("User", backref="created_events")


