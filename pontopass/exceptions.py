# coding: utf-8


class PontopassBaseException(Exception):
    def __init__(self, *args, **kwargs):
        for key, value in kwargs.iteritems():
            setattr(self, key, value)
        super(PontopassBaseException, self).__init__(*args)


class UserAlreadyExists(PontopassBaseException):
    pass


class UserAddingError(PontopassBaseException):
    pass


class UserDeletingError(PontopassBaseException):
    pass


class UserDoesNotExist(PontopassBaseException):
    pass
