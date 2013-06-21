# coding: utf-8
from pontopass.managers.base import Manager


class DeviceManager(Manager):

    user = None

    def add(self, type, value, description='', user=None):
        if not (user or self.user):
            raise TypeError(u'please send the user param')

        if not user:
            user = self.user

        frags = ['manage', 'method', 'insert', user, type, value, description]

        obj = self.request(frags=frags)
        self.parse_status(obj.status)
        return obj

    def list(self, user=None):
        if not (user or self.user):
            raise TypeError(u'please send the user param')

        if not user:
            user = self.user

        frags = ['manage', 'method', 'list', user]

        obj = self.request(frags=frags)
        return obj

    def delete(self, id, user=None):
        if not (user or self.user):
            raise TypeError(u'please send the user param')

        if not user:
            user = self.user

        frags = ['manage', 'method', 'delete', user, id]

        obj = self.request(frags=frags)
        self.parse_status(obj.status)

        if obj.status == 0:
            return True

        return False
