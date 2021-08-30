import numpy as np
from ativacao import Ativacao


class PerceptronMultiCamadas:
    def __init__(self):
        # classe com as ativações e suas derivadas
        self.ativacao = Ativacao()

        self.entradas = np.array([
            [0,0],
            [0,1],
            [1,0],
            [1,1] ])

        # self.saidas = np.array([
        #     [0],
        #     [1],
        #     [1],
        #     [0] ])

        self.saidas = np.array([
            [1],
            [1],
            [1],
            [0] ])

        qtd_neuronios_camada_oculta = 300
        self.apredizagem = 0.3
        self.momento     = 1
        self.epocas      = 3000
        self.resultados  = None

        # 2 neuronios camada entrada, 3 na camada oculta
        self.pesos_camada_oculta = 2 * np.random.random((2, qtd_neuronios_camada_oculta)) -1

        # 3 neuronios camada oculta, 1 na camada saida
        self.pesos_camada_saida = 2 * np.random.random((qtd_neuronios_camada_oculta, 1)) -1


    def calcular(self):
        for epoca in range(self.epocas):
            soma_sinapse_oculta   = np.dot(self.entradas, self.pesos_camada_oculta)
            camada_oculta_ativada = self.ativacao.ativacao(soma_sinapse_oculta)
            soma_sinapse_saida    = np.dot(camada_oculta_ativada, self.pesos_camada_saida)
            camada_saida_ativada  = self.ativacao.ativacao(soma_sinapse_saida)
            self.resultados       = camada_saida_ativada

            # calculo do erro
            erro_camada_saida = self.saidas - camada_saida_ativada
            media_absoluta    = np.mean(np.abs(erro_camada_saida))
            print('Erro: '+str(media_absoluta))

            # calcula Deltas
            delta_saida  = erro_camada_saida * self.ativacao.ativacao_derivada(camada_saida_ativada)
            delta_oculta = (delta_saida.dot(self.pesos_camada_saida.T)) * (self.ativacao.ativacao_derivada(camada_oculta_ativada))

            # calcula novos pesos da camada de saida
            pesos_saida_novos       = camada_oculta_ativada.T.dot(delta_saida)
            self.pesos_camada_saida = (self.pesos_camada_saida * self.momento) + (pesos_saida_novos * self.apredizagem)

            # calcula novos pesos da camada oculta
            pesos_oculta_novos       = self.entradas.T.dot(delta_oculta)
            self.pesos_camada_oculta = (self.pesos_camada_oculta * self.momento) + (pesos_oculta_novos * self.apredizagem)


        print('\n ------------------------ \n ')
        print('Saidas:\n' + str(self.resultados))
        # print('Pesos Camada Saida \n' + str(self.pesos_camada_saida))
        # print('Pesos Camada Oculta \n' + str(self.pesos_camada_oculta))
