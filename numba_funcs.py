import numba

from numba.typed import Dict

def make_numba_dict(dictionary):
    d = Dict()
    for k, v in dictionary.items():
        d[k] = v
    return d