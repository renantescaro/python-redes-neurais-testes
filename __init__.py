import numpy as np
from classes.grafico import Grafico
from classes.parametro import Parametro
from classes.treinamento_perceptron_multi_camadas_numpy import TreinamentoPerceptronMultiCamadas


parametro = Parametro()
parametro.carregar_assets_treinamento()

treinamento = TreinamentoPerceptronMultiCamadas(
    entradas = np.array(parametro.entradas),
    saidas   = np.array(parametro.saidas) )
treinamento.calcular()

Grafico().medias_absolutas(treinamento.medias_absolutas)