##
##
##
import numpy as np
from dpath.util import get as dpget
from dpath.util import set as dpset
from . pass1 import pass1_encrypt, pass1_decrypt

def encrypt(namespace, data):
    namespace = pass1_encrypt(namespace, data)
    return namespace

def decrypt(namespace, *blocks):
    namespace = pass1_decrypt(namespace)
    return dpget(namespace, "/block/cleartext")
