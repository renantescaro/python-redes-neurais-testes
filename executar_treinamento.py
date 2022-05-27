import numpy as np
from classes.ativacao import Ativacao
from classes.dados import Dados
from classes.grafico import Grafico
from classes.imagem import Imagem
from classes.parametro import Parametro
from classes.treinamento_perceptron_multi_camadas_numpy \
    import TreinamentoPerceptronMultiCamadas


porc_erro = 100
dados = Dados(versao=1)
for _ in range(1, 100000):
    treinamento = TreinamentoPerceptronMultiCamadas(
        parametro=Parametro(
            imagem=Imagem()
        ),
        ativacao=Ativacao()
    )
    porc_erro_atual = treinamento.calcular()

    if porc_erro_atual < porc_erro:
        porc_erro = porc_erro_atual
        dados.set('pesos_camada_saida', treinamento.pesos_camada_saida)
        dados.set('pesos_camada_oculta', treinamento.pesos_camada_oculta)

# Grafico().medias_absolutas(treinamento.medias_absolutas)
