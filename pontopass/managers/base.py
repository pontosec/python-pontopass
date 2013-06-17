# coding: utf-8
import requests
from requests.compat import quote


class Manager(object):

    def __init__(self, api_host, api_user, api_pass, api_secure):
        self.api_host = api_host
        self.api_user = api_user
        self.api_pass = api_pass
        self.api_secure = api_secure

    def request(self, path):
        session = requests.Session()
        session.auth = (self.api_user, self.api_pass)

        return session.get(self.build_uri(path=path))

    def build_uri(self, path):
        if self.api_secure:
            schema = 'https://'
        else:
            schema = 'http://'

        uri = '{schema}{host}/{path}/json'.format(
            schema=schema,
            host=self.api_host,
            path=path.strip('/'),
        )

        print uri

        return uri

    def build_path(self, frags):
        frags = map(lambda i: quote(i), frags)
        return '/'.join(frags)
