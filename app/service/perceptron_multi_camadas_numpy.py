import json
import numpy as np
from app.service.dados import Dados
from app.service.ativacoes import AtivacaoContract
from app.service import Parametro


class PerceptronMultiCamadas:
    def __init__(
        self,
        dados: Dados,
        parametro: Parametro,
        ativacao: AtivacaoContract
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

        if self.resultados is None:
            print('\n\n\n sem resultados!')
            return

        print('\n\n\n-------------')
        for linha in self.resultados:
            numero_binario = ''.join(str(round(caracter)) for caracter in linha)
            numero_inteiro = int(numero_binario, 2)

            print(f'{numero_inteiro} {numero_binario}')
            print('-------------')


    def executar(self) -> None:
        self._parametro.executar()
        entradas = np.array(self._parametro.entradas)

        soma_sinapse_oculta   = np.dot(entradas, self.pesos_camada_oculta)
        camada_oculta_ativada = self._ativacao.ativar(soma_sinapse_oculta)
        soma_sinapse_saida    = np.dot(camada_oculta_ativada, self.pesos_camada_saida)
        camada_saida_ativada  = self._ativacao.ativar(soma_sinapse_saida)
        self.resultados       = camada_saida_ativada

        self._mostrar_resultados()
