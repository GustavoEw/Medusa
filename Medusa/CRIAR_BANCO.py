from Medusa import database, app
from Medusa.models import Usuario, Membros

with app.app_context():
    database.create_all()