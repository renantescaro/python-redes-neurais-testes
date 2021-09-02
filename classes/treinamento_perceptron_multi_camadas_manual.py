import json
import numpy as np
from classes.debug import Debug
from classes.ativacao import Ativacao


class TreinamentoPerceptronMultiCamadas:
    def __init__(self, entradas=None, saidas=None):
        # classe com as ativações e suas derivadas
        self.ativacao = Ativacao()

        self.entradas = entradas
        self.saidas   = saidas

        qtd_neuronios_camada_oculta = 500
        self.apredizagem = 0.3
        self.momento     = 1
        self.epocas      = 100000
        self.resultados  = None

        self.pesos_camada_oculta:np.ndarray = 2 * np.random.random((
            len(self.entradas[0]),
            qtd_neuronios_camada_oculta )) -1

        self.pesos_camada_saida:np.ndarray = 2 * np.random.random((
            qtd_neuronios_camada_oculta, 
            len(self.saidas[0]) )) -1


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
        linha_atual = 1
        for linha in self.resultados:
            print(str(round(linha[0]))+' '+
                  str(round(linha[1]))+' '+
                  str(round(linha[2]))+' '+
                  str(round(linha[3]))+' '+
                  str(round(linha[4]))+' '+
                  str(round(linha[5])) )
            if linha_atual == 2:
                print('-----')
                linha_atual = 1
            else:
                linha_atual +=1

        # print('Pesos Camada Saida \n' + str(self.pesos_camada_saida))
        # print('Pesos Camada Oculta \n' + str(self.pesos_camada_oculta))