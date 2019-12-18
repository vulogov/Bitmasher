##
##
##

import numpy as np
from dpath.util import get as dpget
from dpath.util import set as dpset

def make_block(namespace):
    block_size = dpget(namespace, "/config/block.size")
    b = np.random.randint(0,255, size=block_size+8, dtype='B')
    dpset(namespace, "/block/data", b)
    return namespace
