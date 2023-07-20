from Medusa import database, app, login_manager
from datetime import datetime
from flask_login import UserMixin
@login_manager.user_loader

class Usuario(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    email = database.Column(database.String, nullable=False)
    senha = database.Column(database.String, nullable=False)


class Membros(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    numeroDeMatricula = database.Column(database.Integer, nullable=False)
    Nome = database.Column(database.String, nullable=False)
    data_integração = database.Column(database.Date, nullable=False)
    ativo = database.Column(database.Bolean, nullable=False, default=datetime.utcnow())
    imagem = database.Column(database.String, default="default.png")