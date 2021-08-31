import numpy as np
from classes.imagem import Imagem
from classes.treinamento_perceptron_multi_camadas import TreinamentoPerceptronMultiCamadas


entradas = np.array([
    Imagem('assets/0_pequena1.png').array(),
    Imagem('assets/0_pequena2.png').array(),
    Imagem('assets/1_pequena1.png').array(),
    Imagem('assets/1_pequena2.png').array() ])

saidas = np.array([[0], [0], [1], [1]])

# entradas = np.array([[0,0], [0,1], [1,0], [1,1]])
# saidas   = np.array([[0], [1], [1], [0]])

TreinamentoPerceptronMultiCamadas(
    entradas = entradas,
    saidas   = saidas
).calcular()