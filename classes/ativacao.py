import numpy as np


class Ativacao:
    def ativacao(self, soma):
        return self._sigmoid(soma)


    def ativacao_derivada(self, valor_ativacao):
        return self._sigmoid_derivada(valor_ativacao)


    def _re_lu(self, x):
        return x * (x > 0)


    def _re_lu_derivada(self, x):
        return 1. * (x > 0)


    def _leaky_re_lu(self, x):
        return np.where(x > 0, x, x * 0.01).astype(np.float)


    def _leaky_re_lu_derivada(self, x):
        return np.sum([
            ((x > 0) * x),
            ((x <= 0) * x * 0.01)],
            dtype=np.float )


    def _elu(self, x, alpha=1):
        less_than_zero =  (np.zeros_like(x) >= x).astype(np.float)
        less_than_zero *= (np.exp(x) - 1)*alpha
        grt_than_zero  =  (np.zeros_like(x) < x).astype(np.float)
        grt_than_zero  *= x
        return less_than_zero + grt_than_zero


    def _elu_derivada(self, x, alpha=1):
        less_than_zero =  (np.zeros_like(x) >= x).astype(np.float)
        less_than_zero *= self._elu(x)+alpha
        grt_than_zero  =  (np.zeros_like(x) < x).astype(np.float)
        return less_than_zero + grt_than_zero


    def _sigmoid(self, soma):
        return 1 / ( 1 + np.exp(-soma) )
        # with np.errstate(over='raise'):
        #     try:
        #         return 1 / ( 1 + np.exp(-soma) )
        #     except FloatingPointError as e:
        #         print(f'FloatingPointError, soma: {soma}, Except: {e}')


    def _sigmoid_derivada(self, valor_ativacao):
        return valor_ativacao * (1 - valor_ativacao)


    def _tanh(self, x):
        return 2*self._sigmoid(2*x) - 1


    def _tanh_derivada(self, x):
        return 1 - self._tanh(x) ** 2
