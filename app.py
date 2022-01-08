from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from resources.item import Item, ItemList
from resources.user import UserRegister
from resources.store import Store, StoreList
from security import authenticate, identity

# Crear el objeto de la interfaz web
app = Flask(__name__)
# Le dices a sqlalchemy donde va a dejar los datos de la base de datos, en nuestro proyecto
# puede ser sqlite, mysql, psgresql, oracle, ...
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

# Por defecto SQLALQUEMY hace un seguimiento de los cambios en los objetos. Esto solo deja la función básica.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Crear la variable de la key
app.secret_key = 'edu'

# Crear el objeto API
api = Api(app=app)

# Create the object that allow us to check credentials
jwt = JWT(app=app, authentication_handler=authenticate, identity_handler=identity)

api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':  # Asi solo se ejecuta si se ejecuta app.py; si se importa no se ejecuta, pues __name__ sera otro
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
