import numpy as np
from classes.ativacao import Ativacao
from classes.dados import Dados
from classes.grafico import Grafico
from classes.imagem import Imagem
from classes.parametro import Parametro
from classes.treinamento_perceptron_multi_camadas_numpy \
    import TreinamentoPerceptronMultiCamadas


treinamento = TreinamentoPerceptronMultiCamadas(
    dados=Dados(versao=1),
    parametro=Parametro(
        imagem=Imagem()
    ),
    ativacao=Ativacao()
)
treinamento.calcular()

Grafico().medias_absolutas(treinamento.medias_absolutas)
