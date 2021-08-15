class CustomError(Exception):
     def __init__(self, message):
        self.message = message

class RecordNotFoundException(CustomError):
    pass

class PassswordMismatchException(CustomError):
    pass

        