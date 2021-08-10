from flask import jsonify
from flask.views import MethodView

class ProductView(MethodView):
    def get(self):
        return jsonify({"Message":"Hello world"})
    def post(self):
        return jsonify({"POST":"HELLO"})