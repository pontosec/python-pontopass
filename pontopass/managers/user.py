# coding: utf-8
from pontopass.managers.base import Manager


class UserManager(Manager):

    def add(self, user, name=None):
        frags = ['manage', 'user', 'insert', user]
        if name is not None:
            frags += [name]

        path = self.build_path(frags=frags)
        response = self.request(path=path)
        print response
        print response.json()
        return response
