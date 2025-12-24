import sys
import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, BASE_DIR)

from app import app
from extensions import db
from models.event import Event
from datetime import date

def seed_events():
    with app.app_context():
        if Event.query.first():
            print("Zaten etkinlik var")
            return

        e1 = Event(
            title="Sokak Hayvanlarına Yardım",
            description="Mama dağıtımı ve temizlik",
            date=date(2025, 2, 10),
            location="Trabzon"
        )

        e2 = Event(
            title="Fidan Dikimi",
            description="Doğa için fidan dikiyoruz",
            date=date(2025, 3, 5),
            location="KTÜ Kampüsü"
        )

        db.session.add_all([e1, e2])
        db.session.commit()
        print("Etkinlikler eklendi")


if __name__ == "__main__":
    seed_events()
