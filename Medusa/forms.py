# Criar os forms
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, DateField
from wtforms.validators import DataRequired, Email, equal_to, length, ValidationError
from Medusa.Validações import caractere_special
from Medusa.models import Usuario
from flask_wtf.file import FileField, FileRequired
class Formlogin(FlaskForm):
    email = StringField("E-mail",validators=[DataRequired(), Email()] )
    senha = PasswordField("Senha", validators=[DataRequired()])
    botao = SubmitField("Fazer login")

class FormCriarConta(FlaskForm):
    email = StringField("Email", validators= [DataRequired()])
    senha = PasswordField("Senha", validators=[DataRequired(), length(6,20), caractere_special])
    confirmacao_senha =PasswordField("Confirmação de Senha", validators=[DataRequired(), equal_to("senha")])
    botao_confirmacao =SubmitField("Criar conta")

    def validate_email(self, email):
        usuario = Usuario.query.fylter_by(email=email.data).first()
        if usuario:
            return ValidationError("E-mail já cadastrado, faça login para continuar")
        
class Formcriarmembro(FlaskForm):
    nome = StringField("Nome", validators=[DataRequired()])
    numeroDaMatricula = IntegerField("Numero da Matricula", validators=[DataRequired()])
    photo= FileField("Foto")
    dataDeIniciação = DateField("Data De Iniciação", validators=[DataRequired()],format='%d-%m-%Y')
    botao_confirmacao = SubmitField("Criar conta")
   