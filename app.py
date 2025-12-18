from flask import Flask
from config import Config
from extensions import db, login_manager

from routes.main_routes import main
from routes.events import events_bp
from routes.auth import auth_bp

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
login_manager.init_app(app)
login_manager.login_view = "auth.login"

app.register_blueprint(main)
app.register_blueprint(events_bp)
app.register_blueprint(auth_bp)

from models.user import User
from extensions import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

if __name__ == "__main__":
    app.run(debug=True)
