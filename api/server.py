from flask import Flask,jsonify
from flask.views import MethodView
from v1 import register_v1
from mongoengine import connect
from models.product import Product
from setup import initialize
from helpers.utils import CustomJSONEncoder
def create_app():
    app = Flask(__name__)
    app.json_encoder = CustomJSONEncoder
    app.register_blueprint(register_v1('/api/v1'))
    print(f'''     


                   _______      VROOOM!! VROOOM
                 /        |    
         _______/_________|_____________
        /___   API Service : Test Setup |
        |   __                      __  |       
        | /    \------------------/    \| 
          \ __ /                  \ __ /
    
    
    ''')  
    connect(host="mongodb://root:example@mongodb:27017/shop?authSource=admin")
    initialize()
    return app
        # app.run(port=1000,host="0.0.0.0",debug=True)
