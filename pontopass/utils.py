# coding: utf-8
import posixpath
import urlparse


class Object:
    def __init__(self, dict):
        self.__dict__.update(dict)

    def __repr__(self):
        reprkeys = sorted(k for k in self.__dict__.keys() if k[0] != '_')
        info = u", ".join("%s=%s" % (k, repr(getattr(self, k))) for k in reprkeys)
        return u"<%s %s>" % (self.__class__.__name__, info)


def dict2obj(dict):
    return Object(dict)


def url_join(base, *args):
    scheme, netloc, path, query, fragment = urlparse.urlsplit(base)
    path = path if len(path) else "/"

    _args = []
    for arg in args:
        if isinstance(arg, unicode):
            arg = arg.encode('utf8')
        elif isinstance(arg, str):
            arg.decode('utf8')
        _args.append(arg)

    path = posixpath.join(path, *_args)
    return urlparse.urlunsplit([scheme, netloc, path, query, fragment])
