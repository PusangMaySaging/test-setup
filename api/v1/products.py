from flask import jsonify
from flask.views import MethodView
from models.product import Product

class ProductView(MethodView):
    def get(self):
        try:
            products = Product.get() #list of products
            return jsonify({'payload': products})
        except Exception as error:
            print(error)
            return jsonify({'error':error})
    def post(self):
        return jsonify({"POST":"HELLO"})