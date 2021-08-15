from flask import jsonify,request
from flask.views import MethodView
from models.user import User
from helpers.utils import verify_password
from helpers.errors import PassswordMismatchException, RecordNotFoundException
from helpers.http import RESPONSE
class LoginView(MethodView):
    
    def post(self):
        try:
            body = request.get_json()
            user = User.getOne({'email': body.get('email')})

            if(user):
                if verify_password(user.get('password'), body.get('password')):
                    return jsonify({'success':True, 'message': "Successfully Logged in" })
                else:
                    raise PassswordMismatchException("Incorrect Password")

            raise RecordNotFoundException("User does not exists")
        
        except RecordNotFoundException as error:
            print(error.message)
            return jsonify({'success':False, 'message': error.message}), RESPONSE['BAD_REQ']
        except PassswordMismatchException as error:
            print(error.message)
            return jsonify({'success':False, 'message': error.message}), RESPONSE['BAD_REQ']
        except Exception as error:
            print(error.message)
            return jsonify({'success':False, 'message': error.message}), RESPONSE['BAD_REQ']