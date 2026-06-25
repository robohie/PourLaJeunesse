# Ce module contient toutes les opérations que nous pouvons appliquer à un signal.
import numpy as np

def shift_time(fun, a:float, t):
    """Retourne fun(t-a) qui est la version
    temporellement décalée de la fonction fun"""
    t = np.asarray(t)

    return fun(t-a)

def scale_time(fun, a:float, t):
    """Retourne fun(at)"""
    t = np.asarray(t)

    return fun(a * t)

def shift_scale_time(fun, a:float, b:float, t):
    """Retourne fun(at-b)"""
    t = np.asarray(t)

    return fun(a * t - b)