from app.service.ativacoes import (
    Sigmoid, Tanh, LeakyRelu)
from app.service import (
    Imagem, Parametro,
    Dados, Grafico,
    PerceptronMultiCamadas)


rede = PerceptronMultiCamadas(
    dados=Dados(versao=5),
    parametro=Parametro(
        ativacao=Tanh(),
        imagem=Imagem(),
        imagem_unica='assets/uploads/GUC1I97.png'
    )
)
rede.executar()
