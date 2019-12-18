##
##
##
import io
import uuid
import numpy as np
import queue
from dpath.util import new as dpnew
from dpath.util import get as dpget
from dpath.util import set as dpset
from . key import return_key

def cryptobook_init(namespace):
    cryptobook_size = dpget(namespace, "/config/cryptobook.size")
    key_size = dpget(namespace, "/config/key.size")
    dpnew(namespace, "/cryptobook/queue", queue.Queue(cryptobook_size))
    dpnew(namespace, "/cryptobook/used", {})
    for i in range(0,cryptobook_size):
        namespace = cryptobook_add(namespace)
    return namespace

def cryptobook_add(namespace):
    queue = dpget(namespace, "/cryptobook/queue")
    key, masher  = return_key(namespace)
    try:
        queue.put_nowait((str(uuid.uuid4()), key, masher))
    except queue.Full:
        pass
    return namespace

def cryptobook_get(namespace):
    queue = dpget(namespace, "/cryptobook/queue")
    used = dpget(namespace, "/cryptobook/used")
    try:
        id, key, masher = queue.get_nowait()
        used[id] = (key, masher)
        dpset(namespace, "/key/private", key)
        dpset(namespace, "/key/masher", masher)
        dpset(namespace, "/key/id", id)
    except queue.Empty:
        namespace = cryptobook_add(namespace)
        return cryptobook_get(namespace)
    return namespace
