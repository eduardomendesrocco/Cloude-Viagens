from flask import Flask

from config import Config
from controllers.viagens_controller import clima_bp

app = Flask(__name__)

app.secret_key = "CloudeViagens"

app.register_blueprint(clima_bp)

if __name__ == "__main__":
    app.run(debug=True)