##
##
##
import numpy as np
from dpath.util import get as dpget
from dpath.util import set as dpset
from . pass1 import pass1_encrypt, pass1_decrypt
from . pass2 import pass2_encrypt, pass2_decrypt


def encrypt(namespace, data):
    namespace = pass1_encrypt(namespace, data)
    namespace = pass2_encrypt(namespace)
    return namespace

def decrypt(namespace, *blocks):
    namespace = pass2_decrypt(namespace)
    namespace = pass1_decrypt(namespace)
    return dpget(namespace, "/block/cleartext")
