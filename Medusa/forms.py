# Criar os forms
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, equal_to, length, ValidationError
from Medusa.Validações import caractere_special
from Medusa.models import Usuario
caracteres_especiais = ("!", "@","$","%","¨", "&", "*","(",")",",",)
class Formlogin(FlaskForm):
    email = StringField("E-mail",validators=[DataRequired(), Email,()] )
    senha = PasswordField("Senha", validators=[DataRequired()])
    botao = SubmitField("Fazer login")

class FormCriarConta(FlaskForm):
    email = StringField("Email", validators= [DataRequired(), Email,()])
    username =StringField("Username", validators=[DataRequired()])
    senha = PasswordField("Senha", validators=[DataRequired(), length(6,20), caracteres_especiais])
    confirmacao_senha =PasswordField("Confirmação de Senha", validators=[DataRequired(), equal_to("senha")])
    botao_confirmacao =SubmitField("Criar conta")

    def validate_email(self, email):
        usuario = Usuario.query.fylter_by(email=email.data).first()
        if usuario:
            return ValidationError("E-mail já cadastrado, faça login para continuar")