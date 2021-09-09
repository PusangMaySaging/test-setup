import logging
from flask import jsonify,request
from flask.views import MethodView
from models.user import User
from helpers.utils import verify_password
from helpers.errors import PassswordMismatchException, RecordNotFoundException
from mongoengine.errors import ValidationError
from helpers.http import RESPONSE

logging.basicConfig(filename='login.log', level=logging.DEBUG)

class LoginView(MethodView):
    
    def post(self):
        try:
            body = request.get_json()
            user = User.getOne({'email': body.get('email')})
            if(user):
                if verify_password(user.get('password', ''), body.get('password','')):
                    logging.info(f"{user.get('email')}({user.get('_id')}) has logged in")
                    return jsonify({'success':True, 'message': 'Successfully Logged in'})
                else:
                    logging.warning(f"Failed login attempt by: {user.get('email')}")
                    raise PassswordMismatchException("Incorrect Password")
            raise RecordNotFoundException("User does not exists")

        except RecordNotFoundException as error:
            return jsonify({'success':False, 'message': error.message})
        except PassswordMismatchException as error:
            return jsonify({'success':False, 'message': error.message})
        except Exception as error:
            logging.error(str(error))
            return jsonify({'success':False, 'message': error}), RESPONSE['INTERNAL']