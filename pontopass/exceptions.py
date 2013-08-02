# coding: utf-8


class PontopassException(Exception):
    def __init__(self, *args, **kwargs):
        for key, value in kwargs.iteritems():
            setattr(self, key, value)
        super(PontopassException, self).__init__(*args)

    @classmethod
    def get(self, id, *args, **kwargs):
        id = int(id)
        if id in ERRORS:
            raise ERRORS[id](*args, **kwargs)
        return None


class StartError(PontopassException):
    pass


class InvalidCredentials(PontopassException):
    pass


class UnknownError(PontopassException):
    pass


class UserAlreadyExists(PontopassException):
    pass


class InvalidData(PontopassException):
    pass


class UserNotFound(PontopassException):
    pass


class SessionNotFound(PontopassException):
    pass


class InvalidSession(PontopassException):
    pass


class DeviceNotFound(PontopassException):
    pass


class ApplicationNotFound(PontopassException):
    pass


class Unauthorized(PontopassException):
    pass


class InsufficientCredits(PontopassException):
    pass


class LoginError(PontopassException):
    pass


class LoginInactive(PontopassException):
    pass


class ErrorOnCall(PontopassException):
    pass


ERRORS = {
    20: StartError,
    30: InvalidCredentials,
    150: UnknownError,
    151: UserAlreadyExists,
    152: UnknownError,
    153: UnknownError,
    154: UserNotFound,
    155: InvalidData,
    210: UnknownError,
    220: UnknownError,
    310: UnknownError,
    320: UnknownError,
    400: UserNotFound,
    405: UnknownError,
    410: SessionNotFound,
    411: InvalidSession,
    413: InvalidSession,
    415: DeviceNotFound,
    420: InvalidData,
    422: ApplicationNotFound,
    425: InvalidData,
    440: UnknownError,
    450: UnknownError,
    490: Unauthorized,
    492: InvalidData,
    510: ErrorOnCall,
    520: ErrorOnCall,
    530: ErrorOnCall,
    540: ErrorOnCall,
    600: InsufficientCredits,
    710: LoginError,
    720: InvalidData,
    810: LoginInactive,
    820: LoginInactive,
    830: LoginInactive,
    840: LoginInactive,
    999: UnknownError,
}
