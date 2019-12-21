##
##
##
import bitstring
from dpath.util import get as dpget
from dpath.util import set as dpset

def pass3_encrypt(namespace):
    pass2 = dpget(namespace, "/block/pass2")
    dpset(namespace, "/block/pass3", [])
    pass3 = dpget(namespace, "/block/pass3")
    for data, id, key, masher in pass2:
        b = bitstring.BitString(data.tostring())
        c = 0
        for m in masher:
            #print(m,key[c])
            if m is True:
                b.rol(key[c])
            else:
                b.ror(key[c])
            c += 1
        pass3.append((b.tobytes(), id, key, masher))
    return namespace

def pass3_decrypt(namespace):
    dpset(namespace, "/block/pass2", [])
    pass3 = dpget(namespace, "/block/pass3")
    pass2 = dpget(namespace, "/block/pass2")
    for data, id, key, masher in pass3:
        b = bitstring.BitString(data.tostring())
        c = 0
        for m in masher:
            #print(m, key[c])
            if m is True:
                b.ror(key[c])
            else:
                b.rol(key[c])
            c += 1
        pass2.append((b.tobytes(), id, key, masher))
    return namespace
