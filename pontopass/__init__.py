# coding: utf-8


class Pontopass(object):

    PHONE_CALL = 1
    SMS = 2
    MOBILE_TOKEN = 3
    MOBILE_AUTHENTICATION = MOBILE_AUTH = 4

    WITHOUT_WIDGET = 0
    WITH_WIDGET = 1

    def __init__(self, api_user, api_pass, api_host='api.pontopass.com', api_secure=True):
        self.api_host = api_host
        self.api_user = api_user
        self.api_pass = api_pass
        self.api_secure = api_secure

    def __getattr__(self, name):
        try:
            class_name = ''.join([n.title() for n in name.split('_') + ['manager']])
            module = __import__('pontopass.managers.{0}'.format(name), fromlist=[''])
            klass = getattr(module, class_name)
            return klass(
                api_host=self.api_host,
                api_user=self.api_user,
                api_pass=self.api_pass,
                api_secure=self.api_secure,
            )
        except ImportError, AttributeError:
            if name in self.__dict__:
                return self.__dict__.get(name)
            else:
                raise AttributeError
