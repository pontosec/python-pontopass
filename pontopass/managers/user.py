# coding: utf-8
from pontopass.managers.base import Manager


class UserManager(Manager):

    user = None

    def add(self, name=None, user=None):
        user = user or self.user

        frags = ['manage', 'user', 'insert', user]
        if name is not None:
            frags += [name]

        obj = self.request(frags=frags)
        self.parse_status(obj.status)
        return obj

    def delete(self, user=None):
        user = user or self.user
        
        frags = ['manage', 'user', 'delete', user]
        obj = self.request(frags=frags)
        self.parse_status(obj.status)
        return True

    def __call__(self, user):
        self.user = user
        return self

    @property
    def device(self):
        if self.user is None:
            raise AttributeError(u'device called before user assigment')

        from pontopass.managers.device import DeviceManager
        device_manager = DeviceManager(self.api_host, self.api_user, self.api_pass, self.api_secure)
        device_manager.user = self.user
        return device_manager
