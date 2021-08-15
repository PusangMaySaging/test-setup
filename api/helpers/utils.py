from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

def create_hash(password):
    ph = PasswordHasher()
    hashed_password = ph.hash(password)
    return hashed_password

def verify_password(db_password, sent_password):
    try:
        ph = PasswordHasher()
        ph.verify(db_password, sent_password)
        return True
    except VerifyMismatchError:
        return False

