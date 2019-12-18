##
##
##
import time
import uuid
from dpath.util import get as dpget
from dpath.util import set as dpset
from . block import make_block
from . cryptobook import cryptobook_get
from . exception import BitmasherKeysizeException


def next(namespace, **kw):
    dpset(namespace, "/config/stamp", time.time())
    dpset(namespace, "/config/id", str(uuid.uuid4()))
    if (dpget(namespace, "/config/block.size") % 8) != 0 or (dpget(namespace, "/config/key.size") % 8) != 0:
        raise BitmasherKeysizeException
    namespace = cryptobook_get(namespace)
    namespace = make_block(namespace)
    return namespace
