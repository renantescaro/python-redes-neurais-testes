from app.service.ativacoes import Sigmoid, Tanh, LeakyRelu
from random import randrange
from app.service import (
    Imagem, Parametro, Dados,
    Grafico, Registro,
    TreinamentoPerceptronMultiCamadas)


porc_erro = 100
dados = Dados(versao=3)
for _ in range(1, 100000):
    treinamento = TreinamentoPerceptronMultiCamadas(
        ativacao=Sigmoid(),
        registro=Registro(
            cpu='i5-7300HQ',
            vga='GTX 1050',
        ),
        parametro=Parametro(
            imagem=Imagem(),
            apredizagem=0.2,
            epocas=30000,
            qtd_neuronios_camada_oculta=randrange(start=100, stop=700),
            sub_pasta='letras_e_numeros_placas/',
            momento=1,
        ),
    )
    porc_erro_atual = treinamento.executar()

    if porc_erro_atual < porc_erro:
        porc_erro = porc_erro_atual
        dados.set('pesos_camada_saida', treinamento.pesos_camada_saida)
        dados.set('pesos_camada_oculta', treinamento.pesos_camada_oculta)

# Grafico().medias_absolutas(treinamento.medias_absolutas)
