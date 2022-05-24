import os
from typing import Any, List, Tuple
from classes.imagem import Imagem


class Parametro:
    def __init__(self, imagem: Imagem) -> None:
        self.arquivos  = []
        self.entradas  = []
        self.saidas    = []
        self.caminho_entradas = 'assets/treinamento/'
        self.imagem = imagem


    def carregar_assets_treinamento(self) -> Tuple[List, List[List[int]]]:
        self._listar_arquivos()
        self._ler_imagens()

        return self.entradas, self.saidas


    def _listar_arquivos(self) -> None:
        for p, _, files in os.walk(os.path.abspath(self.caminho_entradas)):
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
        saida_numero = [int(bit) for bit in binario]
        self.saidas.append(saida_numero)


    def _caracter_entrada_para_binario(self, caracter:str) -> str:
        try:
            convertido = int(caracter)
        except ValueError:
            convertido = ord(caracter)

        return format(convertido, '08b')
