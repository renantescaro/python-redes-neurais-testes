import numpy as np
import sys
sys.path.append('C:\_TCC_\python-redes-neurais-testes')
from classes.entrada import Entrada
from classes.treinamento_perceptron_multi_camadas import TreinamentoPerceptronMultiCamadas


entrada = Entrada()
entrada.teste()

TreinamentoPerceptronMultiCamadas(
    entradas = np.array(entrada.entradas),
    saidas   = np.array(entrada.saidas)
).calcular()