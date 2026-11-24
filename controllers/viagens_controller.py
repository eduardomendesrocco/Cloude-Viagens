from flask import Blueprint, render_template, request, redirect, url_for, session
from models.data.data_manager import add_viagem, recupera_viagens_user, busca_viagem_id, delete_viagem, update_viagem

viagens_bp = Blueprint("viagens", __name__, url_prefix="/viagens")

@viagens_bp.route("/", methods=["GET", "POST"])
def viagens():
    if not session.get("usuario_id"):
        return redirect(url_for("usuarios.login"))

    if request.method == "POST":
        add_viagem(request.form, session["usuario_id"])
        return redirect(url_for("viagens.viagens"))

    lista = recupera_viagens_user(session["usuario_id"])
    return render_template("viagens.html", viagens=lista)

@viagens_bp.route("/<int:viagem_id>/deletar", methods=["GET", "POST"])
def deletar(viagem_id):
    if not session.get("usuario_id"):
        return redirect(url_for("usuarios.login"))
    
    viagem = busca_viagem_id(viagem_id)

    if viagem and viagem.get("user_id") == session["usuario_id"]:
        delete_viagem(viagem_id)
    return redirect(url_for('viagens.viagens'))


@viagens_bp.route("/<int:viagem_id>/editar", methods=["GET", "POST"])
def editar(viagem_id):
    if not session.get("usuario_id"):
        return redirect(url_for("usuarios.login"))

    viagem = busca_viagem_id(viagem_id)

    if not viagem or viagem.get("user_id") != session["usuario_id"]:
        return redirect(url_for("viagens.viagens"))

    if request.method == "POST":
        update_viagem(viagem_id, request.form)
        return redirect(url_for("viagens.viagens"))

    return render_template("editar_viagem.html", viagem=viagem)