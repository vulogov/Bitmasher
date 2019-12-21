##
##
##
import numpy as np
from dpath.util import get as dpget
from dpath.util import set as dpset

def pass2_encrypt(namespace):
    block_size = dpget(namespace, "/config/block.size")
    pass1 = dpget(namespace, "/block/pass1")
    dpset(namespace, "/block/pass2", [])
    pass2 = dpget(namespace, "/block/pass2")
    for data, id, key, masher in pass1:
        forest = np.random.randint(0, 255, size=len(data)*2, dtype='B')
        forest[::2] = data
        pass2.append((forest, id, key, masher))
    return namespace

def pass2_decrypt(namespace):
    dpset(namespace, "/block/pass1", [])
    pass1 = dpget(namespace, "/block/pass1")
    pass2 = dpget(namespace, "/block/pass2")
    for data, id, key, masher in pass2:
        deforest = data[::2]
        pass1.append((deforest, id, key, masher))
    return namespace
