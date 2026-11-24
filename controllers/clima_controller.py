from flask import Blueprint, render_template, request
from models.clima import buscar_previsao

clima_bp = Blueprint("clima", __name__)
@clima_bp.route("/")
def home():
    cidade = request.args.get("cidade", "").strip()
    previsao = None

    if cidade:
        previsao = buscar_previsao(cidade)

    return render_template("index.html", cidade=cidade, previsao=previsao)