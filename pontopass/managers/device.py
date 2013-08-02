# coding: utf-8
from pontopass import Pontopass
from pontopass.managers.base import Manager


class DeviceManager(Manager):

    user = None
    session_id = None

    def add(self, type, value, description='', user=None):
        user = user or self.user

        frags = ['manage', 'method', 'insert', user, type, value, description]

        obj = self.request(frags=frags)
        self.parse_status(obj.status)
        return obj

    def list(self, user=None, session_id=None, *args, **kwargs):
        user = user or self.user
        session_id = session_id or self.session_id

        if not (user or session_id):
            raise TypeError(u'please send the user or session_id param')

        if user:
            kwargs.update({'user': user})
            return self._list_by_user(*args, **kwargs)
        elif session_id:
            kwargs.update({'session_id': session_id})
            return self._list_by_session(*args, **kwargs)

    def delete(self, device_id, user=None):
        user = user or self.user

        frags = ['manage', 'method', 'delete', user, device_id]

        obj = self.request(frags=frags)
        self.parse_status(obj.status)

        if obj.status == 0:
            return True

        return False

    def ask(self, device_id, user_ip, user_agent, session_id=None):
        session_id = session_id or self.session_id

        frags = ['ask', session_id, device_id, user_ip, user_agent]
        obj = self.request(frags=frags)
        self.parse_status(obj.status)

        if obj.status == 0:
            return True

        return False

    def answer(self, code, type, user_ip, user_agent, session_id=None):
        session_id = session_id or self.session_id

        type_dict = {
            Pontopass.PHONE_CALL: 'telefone',
            Pontopass.SMS: 'sms',
            Pontopass.MOBILE_TOKEN: 'token',
            Pontopass.MOBILE_AUTHENTICATION: 'app'
        }

        type = type_dict.get(int(type))

        frags = ['validate', type, session_id, code, user_ip, user_agent]
        obj = self.request(frags=frags)
        self.parse_status(obj.status)
        return obj

    def _list_by_user(self, user):
        frags = ['manage', 'method', 'list', user]
        obj = self.request(frags=frags)
        return obj

    def _list_by_session(self, user_ip, user_agent, session_id):
        frags = ['list', session_id, user_ip, user_agent]
        obj = self.request(frags=frags)
        obj = self.parse_dict(obj.methods)
        return obj
