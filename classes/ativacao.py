import numpy as np
# import tensorflow as tf


class Ativacao:
    def ativacao(self, soma):
        return self.sigmoid(soma)


    def ativacao_derivada(self, valor_ativacao):
        return self.sigmoid_derivada(valor_ativacao)


    def re_lu(self, x):
        return x * (x > 0)


    def re_lu_derivada(self, x):
        return 1. * (x > 0)


    def leaky_re_lu(self, x):
        return np.where(x > 0, x, x * 0.01).astype(np.float)


    def leaky_re_lu_derivada(self, x):
        return np.sum([
            ((x > 0) * x),
            ((x <= 0) * x * 0.01)],
            dtype=np.float )


    def elu(self, x, alpha=1):
        less_than_zero =  (np.zeros_like(x) >= x).astype(np.float)
        less_than_zero *= (np.exp(x) - 1)*alpha
        grt_than_zero  =  (np.zeros_like(x) < x).astype(np.float)
        grt_than_zero  *= x
        return less_than_zero + grt_than_zero


    def elu_derivada(self, x, alpha=1):
        less_than_zero =  (np.zeros_like(x) >= x).astype(np.float)
        less_than_zero *= self.elu(x)+alpha
        grt_than_zero  =  (np.zeros_like(x) < x).astype(np.float)
        return less_than_zero + grt_than_zero


    def sigmoid(self, soma):
        return 1 / ( 1 + np.exp(-soma) )


    def sigmoid_derivada(self, valor_ativacao):
        return valor_ativacao * (1 - valor_ativacao)


    def tanh(self, x):
        return 2*self.sigmoid(2*x) - 1


    def tanh_derivada(self, x):
        return 1 - self.tanh(x) ** 2
