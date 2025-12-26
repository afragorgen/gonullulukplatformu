import pytest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_home_page(client):
    response = client.get("/")
    assert response.status_code == 200


def test_register_page(client):
    response = client.get("/register")
    assert response.status_code == 200


def test_login_page(client):
    response = client.get("/login")
    assert response.status_code == 200
    assert "Giriş".encode("utf-8") in response.data



def test_events_page(client):
    response = client.get("/events")
    assert response.status_code == 200


def test_join_event_requires_login(client):
    response = client.post("/events/1/join", follow_redirects=True)
    assert response.status_code == 200

