# Criar as rotas do nosso site (os links)
from flask import render_template

from Medusa import app
from flask_login import login_required
from Medusa.forms import FormCriarConta, Formlogin , Formcriarmembro

@app.route("/", methods=['GET, POST'])
def homepage():
    formLogin = Formlogin()
    if formLogin.validate_on_submit():
        pass
    return render_template("homepage.html", form= formLogin)
@app.route("/criar-conta", methods=['GET, POST'])
def criarConta():
    formcriarconta= FormCriarConta()
    return render_template("criarconta.html", form = formcriarconta)
@app.route("/<usuario>", methods=['GET, POST'])
@login_required
def perfil(usuario):
    membro = Formcriarmembro
    return render_template("perfil.html", usuario = usuario, form = Formcriarmembro)

@app.route("/<Membros>")
def membros(Membros):
    return render_template("carteira.html")

    