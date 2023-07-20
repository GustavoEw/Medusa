import re
from wtforms.validators import ValidationError
def caractere_special(form,field):
    passowrd = field.data
    if len(re.findall(r"[. + - * ~ _ @ # :?]", passowrd))<1:
         raise ValidationError("Senha sem caractere especial")

