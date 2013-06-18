# coding: utf-8
from pontopass.managers.base import Manager


class UserManager(Manager):

    def add(self, user, name=None):
        frags = ['manage', 'user', 'insert', user]
        if name is not None:
            frags += [name]

        obj = self.request(frags=frags)
        self.parse_status(obj.status)
        return obj

    def delete(self, user):
        frags = ['manage', 'user', 'delete', user]
        obj = self.request(frags=frags)
        self.parse_status(obj.status)

        if obj.status == 0:
            return True

        return False
