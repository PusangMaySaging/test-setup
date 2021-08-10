from flask import Blueprint,jsonify
from flask.views import MethodView


def register_v1(prefix):
    v1_bp = Blueprint('version_1',__name__,url_prefix=prefix)
    from .products import ProductView
    v1_bp.add_url_rule('/products', view_func=ProductView.as_view('products'))

    return v1_bp


