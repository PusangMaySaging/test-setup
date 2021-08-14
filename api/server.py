from flask import Flask,jsonify
from flask.views import MethodView
from v1 import register_v1
from mongoengine import connect
from models.product import Product
app = Flask(__name__)
print("STARTING SHOP_API")
connect(host="mongodb://root:example@mongodb:27017/shop?authSource=admin")
#connect('shop', host='127.0.0.1', port=27017, username='root', username="example")
# product = Product(name="Nike Shoes")
# product.save()
app.register_blueprint(register_v1('/api/v1'))
if __name__ == "__main__":
    app.run(port=1000,host="0.0.0.0",debug=True)

