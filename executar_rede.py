from app.service.ativacoes import Sigmoid, Tanh
from random import randrange
from app.service import (
    Imagem, Parametro,
    Dados, Grafico,
    PerceptronMultiCamadas)


rede = PerceptronMultiCamadas(
    dados=Dados(versao=4),
    parametro=Parametro(
        ativacao=Tanh(),
        imagem=Imagem(),
        sub_pasta='numeros_placas_teste/'
    )
)
rede.executar()
