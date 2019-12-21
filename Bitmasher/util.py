##
##
##
import io
import numpy as np

def telegram(data):
    _buf = np.frombuffer(data, dtype='B')
    _tlg = _buf.reshape((int(len(_buf)/8), 8))
    res = ""
    for row in _tlg:
        f = io.StringIO()
        np.savetxt(f, row, newline=' ', fmt='%03i')
        res += f.getvalue().strip()+'\n'
    return res
