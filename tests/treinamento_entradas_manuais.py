import numpy as np
from classes.imagem import Imagem
from classes.treinamento_perceptron_multi_camadas import TreinamentoPerceptronMultiCamadas

# Entrada().ler_imagens()

entradas = np.array([
    # 0
    Imagem('assets/treinamento/0_1.png').array(),
    Imagem('assets/treinamento/0_2.png').array(),

    # 1
    Imagem('assets/treinamento/1_1.png').array(),
    Imagem('assets/treinamento/1_2.png').array(),

    # 2
    Imagem('assets/treinamento/2_1.png').array(),
    Imagem('assets/treinamento/2_2.png').array(),

    # 3
    Imagem('assets/treinamento/3_1.png').array(),
    Imagem('assets/treinamento/3_2.png').array(),

    # 4
    Imagem('assets/treinamento/4_1.png').array(),
    Imagem('assets/treinamento/4_2.png').array(),

    # 5
    Imagem('assets/treinamento/5_1.png').array(),
    Imagem('assets/treinamento/5_2.png').array(),

    # 6
    Imagem('assets/treinamento/6_1.png').array(),
    Imagem('assets/treinamento/6_2.png').array(),

    # 7
    Imagem('assets/treinamento/7_1.png').array(),
    Imagem('assets/treinamento/7_2.png').array(),

    # 8
    Imagem('assets/treinamento/8_1.png').array(),
    Imagem('assets/treinamento/8_2.png').array(),

    # 9
    Imagem('assets/treinamento/9_1.png').array(),
    Imagem('assets/treinamento/9_2.png').array(),
], dtype=np.longdouble)

saidas = np.array([
    # 0
    [0,0,0,0,0,0], [0,0,0,0,0,0],

    # 1
    [0,0,0,0,0,1], [0,0,0,0,0,1],

    # 2
    [0,0,0,0,1,0], [0,0,0,0,1,0],

    # 3
    [0,0,0,0,1,1], [0,0,0,0,1,1],

    # 4
    [0,0,0,1,0,0], [0,0,0,1,0,0],

    # 5
    [0,0,0,1,0,1], [0,0,0,1,0,1],

    # 6
    [0,0,0,1,1,0], [0,0,0,1,1,0],

    # 7
    [0,0,0,1,1,1], [0,0,0,1,1,1],

    # 8
    [0,0,1,0,0,0], [0,0,1,0,0,0],

    # 9
    [0,0,1,0,0,1], [0,0,1,0,0,1]
], dtype=np.longdouble)

# entradas = np.array([[0,0], [0,1], [1,0], [1,1]])
# saidas   = np.array([[0], [1], [1], [0]])

TreinamentoPerceptronMultiCamadas(
    entradas = entradas,
    saidas   = saidas
).calcular()