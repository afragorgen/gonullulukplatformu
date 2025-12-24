from flask import Flask
from extensions import db, login_manager
from routes.auth import auth_bp
from routes.events import events_bp
from routes.main_routes import main_bp
from models.user import User

app = Flask(__name__)

app.config["SECRET_KEY"] = "super-secret-key-change-me"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///platform.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
login_manager.init_app(app)
login_manager.login_view = "auth.login"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

app.register_blueprint(main_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(events_bp)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)