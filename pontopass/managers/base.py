# coding: utf-8
import requests
from pontopass.utils import dict2obj, url_join
from pontopass.exceptions import PontopassException


class Manager(object):

    def __init__(self, api_host, api_user, api_pass, api_secure):
        self.api_host = api_host
        self.api_user = api_user
        self.api_pass = api_pass
        self.api_secure = api_secure

    def request(self, path=None, frags=None, parse=True):
        if frags is not None:
            path = self.build_path(frags=frags)

        session = requests.Session()
        session.auth = (self.api_user, self.api_pass)

        response = session.get(self.build_uri(path=path))

        if parse:
            return self.parse_response(response)

        return response

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

        return uri

    def parse_response(self, response):
        data = response.json
        if callable(response.json):
            data = data()

        return self.parse_dict(data)

    def parse_status(self, status):
        PontopassException.get(status)

    def build_path(self, frags):
        return url_join(*frags)

    def parse_dict(self, dict):
        if isinstance(dict, list):
            return map(dict2obj, dict)
        return dict2obj(dict)
