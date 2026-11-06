from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from models.data.data_manager import add_user, busca_user_email

user_bp = Blueprint("usuarios", __name__, url_prefix="/usuarios")


@user_bp.route('cadastrar', methods=["GET", "POST"])
def cadastrar():
    if request.method == "POST":
        res = add_user(request.form)

        if res:
            flash("Usuário cadastrado com sucesso!", "success")

        return redirect(url_for("usuarios.login"))
    
    flash("Preencha todos os dados necessários.", "danger")

    return render_template("formularios.html")



@user_bp.route('login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        senha = request.form.get("senha")

        if not email or not senha:
            flash("Preencha os dados necessários.", "danger")]

        return render_template("formularios.html")
    
    user = busca_user_email(email)

    if user and senha == user["senha"]:
        session["usuario_id"] = user["id"]
        session["usuario_nome"] = user["nome"]

        flash("Login realizado com sucesso!", "success")
    return render_template("formularios.html")