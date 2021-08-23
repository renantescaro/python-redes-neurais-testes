import unittest
import sys
sys.path.append('C:\_TCC_\python-redes-neurais-testes')
from ativacao import Ativacao


class AtivacaoTest:
    def re_lu_test(self, x):
        Ativacao().re_lu(x)


    def re_lu_derivada_test(self, x):
        Ativacao().re_lu_derivada(x)

    
    def leaky_re_lu_test(self, x):
        Ativacao().leaky_re_lu(x)
    

    def leaky_re_lu_derivada_test(self, x):
        Ativacao().leaky_re_lu_derivada(x)


    def sigmoid_test(self, x):
        Ativacao().sigmoid(x)


    def sigmoid_derivada_test(self, x):
        Ativacao().sigmoid_derivada(x)