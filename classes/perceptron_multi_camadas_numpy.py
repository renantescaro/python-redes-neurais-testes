import json
import numpy as np
from classes.dados import Dados
from classes.ativacao import Ativacao
from classes.parametro import Parametro


class PerceptronMultiCamadas:
    def __init__(
        self,
        dados:Dados,
        parametro: Parametro,
        ativacao: Ativacao
    ) -> None:

        # classe com as ativações e suas derivadas
        self._ativacao = ativacao
        self._dados = dados
        self._parametro = parametro

        self.pesos_camada_oculta = self._dados.get('pesos_camada_oculta')
        self.pesos_camada_saida = self._dados.get('pesos_camada_saida')

        self.resultados  = None
        self.medias_absolutas = []


    def calcular(self) -> None:
        self._parametro.carregar_assets_treinamento()
        entradas = np.array(self._parametro.entradas)

        soma_sinapse_oculta   = np.dot(entradas, self.pesos_camada_oculta)
        camada_oculta_ativada = self._ativacao.ativacao(soma_sinapse_oculta)
        soma_sinapse_saida    = np.dot(camada_oculta_ativada, self.pesos_camada_saida)
        camada_saida_ativada  = self._ativacao.ativacao(soma_sinapse_saida)
        self.resultados       = camada_saida_ativada

        # resultados
        print('\n ------------------------ \n ')
        linha_atual = 1
        for linha in self.resultados:
            print(
                str(round(linha[0]))+' '+
                str(round(linha[1]))+' '+
                str(round(linha[2]))+' '+
                str(round(linha[3]))+' '+
                str(round(linha[4]))+' '+
                str(round(linha[5]))+' '+
                str(round(linha[6]))
            )
            if linha_atual == 2:
                print('-----')
                linha_atual = 1
            else:
                linha_atual +=1

        # print('Pesos Camada Saida \n' + str(self.pesos_camada_saida))
        # print('Pesos Camada Oculta \n' + str(self.pesos_camada_oculta))
