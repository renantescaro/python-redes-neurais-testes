import numpy as np


class Ativacao:
    def ativacao(self, soma):
        return self.leaky_re_lu(soma)


    def ativacao_derivada(self, valor_ativacao):
        return self.leaky_re_lu_derivada(valor_ativacao)


    def re_lu(self, x):
        return x * (x > 0)


    def re_lu_derivada(self, x):
        return 1. * (x > 0)

    
    def leaky_re_lu(self, x):
        return np.where(x > 0, x, x * 0.01)
    

    def leaky_re_lu_derivada(self, x):
        dx = np.ones_like(x)
        dx[x < 0] = 0.01
        return dx


    def sigmoid(self, soma):
        return 1 / ( 1 + np.exp(-soma) )


    def sigmoid_derivada(self, valor_ativacao):
        return valor_ativacao * (1 - valor_ativacao)