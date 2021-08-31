import unittest
import sys
sys.path.append('C:\_TCC_\python-redes-neurais-testes')
from classes.ativacao import Ativacao


class AtivacaoTest:
    def re_lu_test(self, x):
        return Ativacao().re_lu(x)

    def re_lu_derivada_test(self, x):
        return Ativacao().re_lu_derivada(x)

    
    def leaky_re_lu_test(self, x):
        return Ativacao().leaky_re_lu(x)
    

    def leaky_re_lu_derivada_test(self, x):
        return Ativacao().leaky_re_lu_derivada(x)


    def sigmoid_test(self, x):
        return Ativacao().sigmoid(x)


    def sigmoid_derivada_test(self, x):
        return Ativacao().sigmoid_derivada(x)

aaa = AtivacaoTest().sigmoid_test(-1)
print(aaa)