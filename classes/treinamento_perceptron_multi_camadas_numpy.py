import pickle
import numpy as np
from classes.dados import Dados
from classes.ativacao import Ativacao
from classes.parametro import Parametro


class TreinamentoPerceptronMultiCamadas:
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

        self._parametro.carregar_assets_treinamento()
        self.entradas = np.array(self._parametro.entradas)
        self.saidas = np.array(self._parametro.saidas)

        qtd_neuronios_camada_oculta = 300
        self.apredizagem = 0.3
        self.momento     = 1
        self.epocas      = 20000
        self.resultados  = None
        self.medias_absolutas = []

        self.pesos_camada_oculta:np.ndarray = 2 * np.random.random((
            len(self.entradas[0]),
            qtd_neuronios_camada_oculta
        )) -1

        self.pesos_camada_saida:np.ndarray = 2 * np.random.random((
            qtd_neuronios_camada_oculta,
            len(self.saidas[0])
        )) -1

        # self.pesos_camada_oculta = self._dados.get('pesos_camada_oculta')
        # self.pesos_camada_saida = self._dados.get('pesos_camada_saida')


    def calcular(self) -> None:
        for epoca in range(self.epocas):
            soma_sinapse_oculta   = np.dot(self.entradas, self.pesos_camada_oculta)
            camada_oculta_ativada = self._ativacao.ativacao(soma_sinapse_oculta)
            soma_sinapse_saida    = np.dot(camada_oculta_ativada, self.pesos_camada_saida)
            camada_saida_ativada  = self._ativacao.ativacao(soma_sinapse_saida)
            self.resultados       = camada_saida_ativada

            # calculo do erro
            erro_camada_saida = np.subtract(self.saidas, camada_saida_ativada)
            media_absoluta    = np.mean(np.abs(erro_camada_saida))
            print(media_absoluta)
            self.medias_absolutas.append((media_absoluta*100))

            # calcula Deltas
            delta_saida  = np.multiply(erro_camada_saida, self._ativacao.ativacao_derivada(camada_saida_ativada))
            delta_oculta = np.multiply((delta_saida.dot(self.pesos_camada_saida.T)), (self._ativacao.ativacao_derivada(camada_oculta_ativada)))

            # calcula novos pesos da camada de saida
            pesos_saida_novos       = camada_oculta_ativada.T.dot(delta_saida)
            self.pesos_camada_saida = np.add(np.multiply(self.pesos_camada_saida, self.momento), np.multiply(pesos_saida_novos, self.apredizagem))

            # calcula novos pesos da camada oculta
            pesos_oculta_novos       = self.entradas.T.dot(delta_oculta)
            self.pesos_camada_oculta = np.add(np.multiply(self.pesos_camada_oculta, self.momento), np.multiply(pesos_oculta_novos, self.apredizagem))


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

        self._dados.set('pesos_camada_saida', self.pesos_camada_saida)
        self._dados.set('pesos_camada_oculta', self.pesos_camada_oculta)

        # print('Pesos Camada Saida \n' + str(self.pesos_camada_saida))
        # print('Pesos Camada Oculta \n' + str(self.pesos_camada_oculta))
