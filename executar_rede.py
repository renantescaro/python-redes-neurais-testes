from classes.ativacao import Ativacao
from classes.dados import Dados
from classes.parametro import Parametro
from classes.perceptron_multi_camadas_numpy import \
    PerceptronMultiCamadas


rede = PerceptronMultiCamadas(
    dados=Dados(versao=1),
    parametro=Parametro(),
    ativacao=Ativacao()
)
rede.calcular()
