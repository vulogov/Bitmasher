##
##
##
import numpy as np
import msgpack
import struct
from dpath.util import get as dpget
from dpath.util import set as dpset
from . next import next as bm_next

def pass1_encrypt(namespace, data=None):
    block_size = dpget(namespace, "/config/block.size")
    d = msgpack.dumps(data)
    namespace = bm_next(namespace)
    _d = [d[i:i+block_size] for i in range(0, len(d), block_size)]
    dpset(namespace, "/block/pass1", [])
    pass1_data = dpget(namespace, "/block/pass1")
    for block in _d:
        block_size = np.fromstring(struct.pack('l', len(block)), dtype='B')
        b_block = dpget(namespace, "/block/data")
        key = dpget(namespace, "/key/private")
        masher = dpget(namespace, "/key/masher")
        id = dpget(namespace, "/key/id")
        src_block = np.fromstring(block, dtype='B')
        b_block[:8] = block_size
        c = 0
        k = 0
        key_size = len(key)
        for e in b_block[:8]:
            b_block[c] = key[k] ^ e
            c += 1
            k += 1
            if k >= key_size:
                k = 0
        c = 0
        for e in src_block:
            if k >= key_size:
                k = 0
            src_block[c] = key[k] ^ e
            c += 1
            k += 1

        b_block[8:len(src_block)+8] = src_block
        pass1_data.append((b_block, id, key, masher))
    return namespace

def pass1_decrypt(namespace):
    block_size = dpget(namespace, "/config/block.size")
    pass1_data = dpget(namespace, "/block/pass1")
    total_data = b""
    for block, id, key, masher in pass1_data:
        c = 0
        k = 0
        d = []
        key_size = len(key)
        for e in block[:8]:
            d.append(key[k] ^ e)
            k += 1
            if k >= key_size:
                k = 0
        data_size = struct.unpack('l', np.array(d, dtype='B').tostring())[0]
        d = []
        for e in block[8:data_size+8]:
            if k >= key_size:
                k = 0
            d.append(key[k] ^ e)
            k += 1
        total_data += np.array(d, dtype='B').tostring()
    data = msgpack.loads(total_data)
    dpset(namespace, "/block/cleartext", data)
    return namespace
