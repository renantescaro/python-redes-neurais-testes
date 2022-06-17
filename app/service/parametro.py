import os
from typing import Any, List, Optional, Tuple
from app.service.ativacoes.ativacao_contract import AtivacaoContract
from app.service.imagem import Imagem


class Parametro:
    def __init__(
        self,
        imagem: Imagem,
        ativacao: AtivacaoContract,
        apredizagem: float= 0.1,
        epocas: int= 1,
        momento: int= 1,
        sub_pasta: str='',
        qtd_neuronios_camada_oculta: int= 1,
    ) -> None:
        self.arquivos = []
        self.entradas = []
        self.saidas = []
        self.imagem = imagem
        self.ativacao = ativacao
        self.apredizagem = apredizagem
        self.epocas = epocas
        self.momento = momento
        self.qtd_neuronios_camada_oculta = qtd_neuronios_camada_oculta
        self.caminho_entradas = f'assets/treinamento/{sub_pasta}'


    def executar(self) -> Tuple[List, List[List[int]]]:
        self._listar_arquivos()
        self._ler_imagens()
        return self.entradas, self.saidas


    def _listar_arquivos(self) -> None:
        for _, _, files in os.walk(os.path.abspath(self.caminho_entradas)):
            for file in files:
                self.arquivos.append(file)


    def _ler_imagens(self) -> None:
        for nome_imagem_com_extensao in self.arquivos:
            self._montar_entradas(nome_imagem_com_extensao)
            self._montar_saidas(nome_imagem_com_extensao)


    def _montar_entradas(self, nome_imagem_com_extensao:str) -> None:
        entrada = self.imagem.converter_np_array(
            caminho_arquivo=f'{self.caminho_entradas}{nome_imagem_com_extensao}'
        )
        self.entradas.append(entrada)


    def _montar_saidas(self, nome_imagem_com_extensao:str) -> None:
        nome = nome_imagem_com_extensao.replace('.png', '')
        caracter_entrada, _ = nome.split('_')
        binario = self._caracter_entrada_para_binario(caracter_entrada)
        saida_numero = None

        if str(self.ativacao) == 'sigmoid':
            saida_numero = [int(bit) for bit in binario]

        if str(self.ativacao) == 'tanh':
            saida_numero = [-1 if int(bit) == 0 else 1 for bit in binario]

        self.saidas.append(saida_numero)


    def _caracter_entrada_para_binario(self, caracter:str) -> str:
        try:
            convertido = int(caracter)
        except ValueError:
            convertido = ord(caracter)

        return format(convertido, '08b')
