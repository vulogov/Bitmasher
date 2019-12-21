##
##
##
import numpy as np
from dpath.util import get as dpget
from dpath.util import set as dpset
from . pass1 import pass1_encrypt, pass1_decrypt
from . pass2 import pass2_encrypt, pass2_decrypt
from . pass3 import pass3_encrypt, pass3_decrypt
from . exception import BitmasherMissedKeyException



def encrypt(namespace, data):
    namespace = pass1_encrypt(namespace, data)
    namespace = pass2_encrypt(namespace)
    namespace = pass3_encrypt(namespace)
    pass3 = dpget(namespace, "/block/pass3")
    out = []
    for data, id, key, masher in pass3:
        out.append((id, data))
    return out

def decrypt(namespace, *blocks):
    dpset(namespace, "/block/pass3", [])
    pass3 = dpget(namespace, "/block/pass3")
    used = dpget(namespace, "/cryptobook/used")
    for id, data in blocks:
        if id not in used:
            raise BitmasherMissedKeyException
        pass3.append((np.frombuffer(data, dtype='B'), id, used[id][0], used[id][1]))
    namespace = pass3_decrypt(namespace)
    namespace = pass2_decrypt(namespace)
    namespace = pass1_decrypt(namespace)
    return dpget(namespace, "/block/cleartext")
