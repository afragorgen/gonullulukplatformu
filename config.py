class Config:
    SECRET_KEY = "super-secret-key"
    SQLALCHEMY_DATABASE_URI = "sqlite:///platform.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

# 🔴 GMAIL SMTP
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = "seninmailin@gmail.com"
    MAIL_PASSWORD = "GMAIL_APP_PASSWORD"
    MAIL_DEFAULT_SENDER = "Gönüllülük Platformu <seninmailin@gmail.com>"