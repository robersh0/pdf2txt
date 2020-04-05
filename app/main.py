from flask import Flask
from app.rest import pdf2text_rest
from app.settings import LocalConfig


def create_app(config_object=LocalConfig):
    app = Flask(__name__, root_path='./')
    app.config.from_object(config_object)
    app.register_blueprint(pdf2text_rest.blueprint)
    return app
