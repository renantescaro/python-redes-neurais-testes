from typing import Optional
import numpy as np
from app.service.dados import Dados
from app.service import Parametro
from app.utils.converter import Converter


class PerceptronMultiCamadas:
    def __init__(
        self,
        dados: Dados,
        parametro: Parametro,
    ) -> None:
        self._dados = dados
        self._parametro = parametro
        self._ativacao = self._parametro.ativacao
        self.pesos_camada_oculta = self._dados.get('pesos_camada_oculta')
        self.pesos_camada_saida = self._dados.get('pesos_camada_saida')

        self.resultados  = None
        self.medias_absolutas = []


    def _processar_resultados(self) -> Optional[str]:
        """
            imprime no console o resultado formatado
            e retorna resultado
        """

        if self.resultados is None:
            print('\n\n\n sem resultados!')
            return None

        for linha in self.resultados:
            binario = ''
            for caracter in linha:
                caracter = 1 if round(caracter) > 0 else 0
                binario += str(round(caracter))

            # treinamento de placa inteira
            if len(binario) == 56:
                # adiciona espaço em branco a cada 8 caracteres
                binario_separados = ' '.join(binario[i:i + 8] for i in range(0, len(binario), 8))

                total = ''
                for byte in binario_separados.split(' '):
                    digito_str = Converter.bits_para_caracter(byte)
                    print(f'{byte} -> {digito_str} ')
                    total += digito_str
                return total

            # treinamento caracter
            else:
                print(f'{binario}')
                return binario


    def executar(self) -> Optional[str]:
        self._parametro.executar_prod()
        entradas = np.array(self._parametro.entradas)

        soma_sinapse_oculta   = np.dot(entradas, self.pesos_camada_oculta)
        camada_oculta_ativada = self._ativacao.ativar(soma_sinapse_oculta)
        soma_sinapse_saida    = np.dot(camada_oculta_ativada, self.pesos_camada_saida)
        camada_saida_ativada  = self._ativacao.ativar(soma_sinapse_saida)
        self.resultados       = camada_saida_ativada

        return self._processar_resultados()
