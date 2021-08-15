from flask import Flask,jsonify
from flask.views import MethodView
from v1 import register_v1
from mongoengine import connect
from models.product import Product
from setup import initialize
app = Flask(__name__)

app.register_blueprint(register_v1('/api/v1'))

if __name__ == "__main__":
    print("STARTING SHOP_API")
    connect(host="mongodb://root:example@mongodb:27017/shop?authSource=admin")
    initialize()
    app.run(port=1000,host="0.0.0.0",debug=True)

