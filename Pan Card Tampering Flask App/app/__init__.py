from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)


if app.config.get("ENV", "development") == "production":
    app.config.from_object("config.DevelopmentConfig")
elif app.config["ENV"] == "testing":
    app.config.from_object("config.TestingConfig")
else:
    app.config.from_object("config.ProductionConfig")

from app import views
