from app.service.ativacoes import Sigmoid
from random import randrange
from app.service import (
    Imagem, Parametro,
    Dados, Grafico,
    PerceptronMultiCamadas)


rede = PerceptronMultiCamadas(
    dados=Dados(versao=3),
    parametro=Parametro(
        imagem=Imagem(),
        sub_pasta='numeros_placas_teste/'
    ),
    ativacao=Sigmoid()
)
rede.executar()
