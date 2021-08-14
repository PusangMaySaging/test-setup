from flask import jsonify
from flask.views import MethodView
from models.product import Product
from helpers import serialize_dict_list
class ProductView(MethodView):
    def get(self):
        try:
            products = serialize_dict_list(Product.objects().as_pymongo()) #list of products
            return jsonify({'payload': products})
        except Exception as error:
            print(error)
            return jsonify({'error':"BAD REQUEST"})
    def post(self):
        return jsonify({"POST":"HELLO"})