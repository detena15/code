from app import app
from db import db

db.init_app(app)


# Este decorador viene con flask. Se va a ejecutar antes de la primera request
@app.before_first_request
def create_tables():
    db.create_all()
    # Crea data.db si no existe. Pero solo crea las tablas que vea: por ejemplo, al importar Store resource,
    # a su vez importa StoreModel, siendo esta la clase que crea la tabla
