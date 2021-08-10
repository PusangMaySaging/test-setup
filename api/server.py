from flask import Flask,jsonify
from flask.views import MethodView
from v1 import register_v1
app = Flask(__name__)


app.register_blueprint(register_v1('/api/v1'))
print("HELLO WORLD")
if __name__ == "__main__":
    app.run(port=1000,host="0.0.0.0",debug=True)