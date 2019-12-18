##
##
##
import uuid
import numpy as np
from dpath.util import get as dpget
from dpath.util import set as dpset

def genkey(namespace):
    key_size = dpget(namespace, "/config/key.size")
    key, masher = return_key(namespace)
    dpset(namespace, "/key/private", key)
    dpset(namespace, "/key/masher", masher)
    dpset(namespace, "/key/id", str(uuid.uuid4()))
    return namespace

def return_key(namespace):
    key_size = dpget(namespace, "/config/key.size")
    k = np.random.randint(0,255, size=key_size, dtype='B')
    m = np.random.randint(2, size=key_size, dtype='?')
    return (k, m)
