from flask import Flask, redirect, url_for

from controllers.viagens_controller import viagens_bp
from controllers.usuarios_controller import user_bp
from controllers.clima_controller import clima_bp

app = Flask(__name__)

app.secret_key = "CloudeViagens"


app.register_blueprint(viagens_bp)
app.register_blueprint(user_bp)
app.register_blueprint(clima_bp)

@app.route("/")
def main():
    return redirect(url_for("usuarios.login"))

if __name__ == "__main__":
    app.run(debug=True)