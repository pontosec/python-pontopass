# coding: utf-8
from pontopass import Pontopass
from pontopass.managers.base import Manager


class SessionManager(Manager):

    def init(self, user, user_ip, user_agent, remember=False, integration_type=Pontopass.WITHOUT_WIDGET):
        frags = ['init', user, integration_type, int(remember), user_ip, user_agent]

        obj = self.request(frags=frags)
        self.parse_status(obj.status)

        return obj.session

    def status(self, session_id, user_ip, user_agent):
        frags = ['status', session_id, user_ip, user_agent]

        obj = self.request(frags=frags)
        self.parse_status(obj.status)

        return obj

    def check(self, user, session_id, user_ip, user_agent):
        frags = ['check', session_id, user_ip, user_agent]

        obj = self.request(frags=frags)
        self.parse_status(obj.status)

        if obj.status == 0 and user == obj.user:
            return True
        return False

    def __call__(self, id):
        self.id = id
        return self

    @property
    def device(self):
        if self.id is None:
            raise AttributeError(u'device called before session_id assigment')

        from pontopass.managers.device import DeviceManager
        device_manager = DeviceManager(self.api_host, self.api_user, self.api_pass, self.api_secure)
        device_manager.session_id = self.id
        return device_manager
