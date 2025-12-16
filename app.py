from flask import Flask
from config import Config

from routes.main_routes import main
from routes.events import events_bp
from routes.auth import auth_bp



from models.user import User
from models.event import Event
from extensions import db


app = Flask(__name__)
app.config.from_object(Config)
app.secret_key = "super-secret-key"



db.init_app(app)

app.register_blueprint(main)
app.register_blueprint(events_bp)
app.register_blueprint(auth_bp)



if __name__ == "__main__":
    app.run(debug=True)

