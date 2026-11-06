from flask import Flask

from controllers.viagens_controller import viagens_bp
from controllers.usuarios_controller import user_bp

app = Flask(__name__)

app.secret_key = "CloudeViagens"

app.register_blueprint(viagens_bp)
app.register_blueprint(user_bp)

if __name__ == "__main__":
    app.run(debug=True)