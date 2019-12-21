##
##
##
import time
import uuid
from dpath.util import new as dpnew
from dpath.util import get as dpget
from dpath.util import set as dpset
from . next import next as bm_next
from . crypto import encrypt, decrypt
from . cryptobook import cryptobook_init, cryptobook_save, cryptobook_load, cryptobook_write
from . util import telegram

def init(*codebooks, **kw):
    namespace = {}
    dpnew(namespace, "/config", {})
    dpnew(namespace, "/cryptobook", {})
    dpnew(namespace, "/config/key.size", 2048)
    dpnew(namespace, "/config/block.size", 1024)
    dpnew(namespace, "/config/stamp", time.time())
    dpnew(namespace, "/config/id", str(uuid.uuid4()))
    dpnew(namespace, "/config/cryptobook.size", 1024)
    dpnew(namespace, "/key", {})
    dpnew(namespace, "/block", {})
    dpnew(namespace, "/block/data", None)
    dpnew(namespace, "/block/cleartext", None)
    dpnew(namespace, "/block/pass1", None)
    dpnew(namespace, "/block/pass2", None)
    dpnew(namespace, "/block/pass3", None)
    dpnew(namespace, "/key/private", b'')
    dpnew(namespace, "/key/masher", b'')
    dpnew(namespace, "/key/id", None)
    dpget(namespace, "/config").update(**kw)
    namespace = cryptobook_init(namespace)
    for cb in codebooks:
        if isinstance(cb, str) is True:
            cryptobook_load(namespace, cb)
        elif hasattr(fp, 'read') is True:
            cryptobook_load(namespace, cb.read())
        else:
            pass
    namespace = bm_next(namespace)
    return namespace
