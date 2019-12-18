##
##
##
import time
import uuid
from dpath.util import new as dpnew
from dpath.util import get as dpget
from dpath.util import set as dpset
from . key import genkey
from . block import make_block
from . next import next as bm_next
from . crypto import encrypt, decrypt
from . cryptobook import cryptobook_init, cryptobook_save

def init(**kw):
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
    namespace = cryptobook_init(namespace)
    namespace = bm_next(namespace)
    dpget(namespace, "/config").update(**kw)
    return namespace
