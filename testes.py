import numpy as np

def sigmoid(soma):
    return 1 / ( 1 + np.exp(-soma) )


def re_lu(x):
    return x * (x > 0)


def re_lu_derivada(x):
    return 1. * (x > 0)


def leaky_re_lu(x):
        return np.where(x > 0, x, x * 0.01)
    

def leaky_re_lu_derivada(x):
    dx = np.ones_like(x)
    dx[x < 0] = 0.01
    return dx

print(leaky_re_lu_derivada(100))