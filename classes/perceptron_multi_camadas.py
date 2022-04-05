import numpy as np
from ativacao import Ativacao


class PerceptronMultiCamadas:
    def __init__(
        self,
        entradas=None,
        saidas=None,
        pesos_camada_oculta=None,
        pesos_camada_saida=None
    ) -> None:

        self.entradas            = entradas
        self.saidas              = saidas
        self.pesos_camada_oculta = pesos_camada_oculta
        self.pesos_camada_saida  = pesos_camada_saida

        self.ativacao   = Ativacao()
        self.resultados = None


    def calcular(self) -> None:
        soma_sinapse_oculta   = np.dot(self.entradas, self.pesos_camada_oculta)
        camada_oculta_ativada = self.ativacao.ativacao(soma_sinapse_oculta)
        soma_sinapse_saida    = np.dot(camada_oculta_ativada, self.pesos_camada_saida)
        camada_saida_ativada  = self.ativacao.ativacao(soma_sinapse_saida)
        self.resultados       = camada_saida_ativada

        # calculo do erro
        erro_camada_saida = self.saidas - camada_saida_ativada
        media_absoluta    = np.mean(np.abs(erro_camada_saida))


        print('Erro: '+str(media_absoluta))
        print('\n ------------------------ \n ')
        print('Saida 1 :\n' + str(self.resultados[0]))
        print('Saida 2 :\n' + str(self.resultados[1]))
        print('Saida 3 :\n' + str(self.resultados[2]))
        print('Saida 4 :\n' + str(self.resultados[3]))
        # print('Pesos Camada Saida \n' + str(self.pesos_camada_saida))
        # print('Pesos Camada Oculta \n' + str(self.pesos_camada_oculta))
