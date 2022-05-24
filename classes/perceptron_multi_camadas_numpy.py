import json
import numpy as np
from classes.dados import Dados
from classes.ativacao import Ativacao
from classes.parametro import Parametro


class PerceptronMultiCamadas:
    def __init__(
        self,
        dados: Dados,
        parametro: Parametro,
        ativacao: Ativacao
    ) -> None:

        self._ativacao = ativacao
        self._dados = dados
        self._parametro = parametro

        self.pesos_camada_oculta = self._dados.get('pesos_camada_oculta')
        self.pesos_camada_saida = self._dados.get('pesos_camada_saida')

        self.resultados  = None
        self.medias_absolutas = []


    def _mostrar_resultados(self):
        """
            imprime no console o resultado formatado
        """

        print('\n\n\n-------------')
        linha_atual = 1
        for linha in self.resultados:

            fila = ''.join(f'{round(caracter)} ' for caracter in linha)
            print(fila)

            if linha_atual == 2:
                print('-------------')
                linha_atual = 1
            else:
                linha_atual +=1


    def calcular(self) -> None:
        self._parametro.carregar_assets_treinamento()
        entradas = np.array(self._parametro.entradas)

        soma_sinapse_oculta   = np.dot(entradas, self.pesos_camada_oculta)
        camada_oculta_ativada = self._ativacao.ativacao(soma_sinapse_oculta)
        soma_sinapse_saida    = np.dot(camada_oculta_ativada, self.pesos_camada_saida)
        camada_saida_ativada  = self._ativacao.ativacao(soma_sinapse_saida)
        self.resultados       = camada_saida_ativada

        self._mostrar_resultados()
