import pickle
import numpy as np
from classes.dados import Dados
from classes.ativacao import Ativacao
from classes.parametro import Parametro


class TreinamentoPerceptronMultiCamadas:
    def __init__(
        self,
        dados: Dados,
        parametro: Parametro,
        ativacao: Ativacao
    ) -> None:

        self._ativacao = ativacao
        self._dados = dados
        self._parametro = parametro

        self._parametro.carregar_assets_treinamento()
        self.entradas = np.array(self._parametro.entradas)
        self.saidas = np.array(self._parametro.saidas)

        qtd_neuronios_camada_oculta = 300
        self.apredizagem = 0.3
        self.momento     = 1
        self.epocas      = 30000
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


    def _delta_saida(self, erro_camada_saida, camada_saida_ativada):
        """
            resultado da multiplicação entre o erro da camada de saida
            com a derivada da camada de saída ativada
        """
        return np.multiply(
            erro_camada_saida,
            self._ativacao.ativacao_derivada(camada_saida_ativada)
        )


    def _delta_oculta(self, delta_saida, camada_oculta_ativada):
        """
            ( delta de saida multiplicado pela tranposta dos pesos da camada de saida )
            multiplicado pela
            ( derivada da camada oculta ativada)
        """
        return np.multiply(
            delta_saida.dot(self.pesos_camada_saida.T),
            self._ativacao.ativacao_derivada(camada_oculta_ativada)
        )


    def _novos_pesos(self, pesos_antigos, pesos_novos):
        """
            ( multiplicação dos pesos antigos com o momento )
            somado a
            ( multiplicação dos pesos novos com a aprendizagem )
        """
        return np.add(
            np.multiply(pesos_antigos, self.momento),
            np.multiply(pesos_novos, self.apredizagem)
        )


    def _mostrar_resultados(self):
        """
            imprime no console o resultado formatado
        """

        print('\n\n\n-------------')
        for index, linha in enumerate(self.resultados, start=1):
            numero_binario = ''.join(str(round(caracter)) for caracter in linha)
            numero_inteiro = int(numero_binario, 2)


            if (index % 2) == 0:
                print(f'{numero_inteiro} {numero_binario}')
                print('-------------')


    def calcular(self) -> None:
        for _ in range(self.epocas):
            soma_sinapse_oculta   = np.dot(self.entradas, self.pesos_camada_oculta)
            camada_oculta_ativada = self._ativacao.ativacao(soma_sinapse_oculta)
            soma_sinapse_saida    = np.dot(camada_oculta_ativada, self.pesos_camada_saida)
            camada_saida_ativada  = self._ativacao.ativacao(soma_sinapse_saida)
            self.resultados       = camada_saida_ativada

            # calculo do erro
            erro_camada_saida = np.subtract(self.saidas, camada_saida_ativada)
            media_absoluta    = np.mean(np.abs(erro_camada_saida))
            self.medias_absolutas.append((media_absoluta*100))
            print('% erro ',media_absoluta*100)

            # calcula Deltas
            delta_saida  = self._delta_saida(erro_camada_saida, camada_saida_ativada)
            delta_oculta = self._delta_oculta(delta_saida, camada_oculta_ativada)

            # calcula novos pesos da camada de saida
            pesos_saida_novos = camada_oculta_ativada.T.dot(delta_saida)
            self.pesos_camada_saida = self._novos_pesos(self.pesos_camada_saida, pesos_saida_novos)

            # calcula novos pesos da camada oculta
            pesos_oculta_novos       = self.entradas.T.dot(delta_oculta)
            self.pesos_camada_oculta = self._novos_pesos(self.pesos_camada_oculta, pesos_oculta_novos)

        self._mostrar_resultados()        

        self._dados.set('pesos_camada_saida', self.pesos_camada_saida)
        self._dados.set('pesos_camada_oculta', self.pesos_camada_oculta)

        # print('Pesos Camada Saida \n' + str(self.pesos_camada_saida))
        # print('Pesos Camada Oculta \n' + str(self.pesos_camada_oculta))
