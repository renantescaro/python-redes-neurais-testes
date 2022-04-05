import os
import numpy as np
from classes.imagem import Imagem

class Parametro:
    def __init__(self) -> None:
        self.arquivos  = []
        self.entradas  = []
        self.saidas    = []
        self.caminho_entradas = 'assets/treinamento/'


    def carregar_assets_treinamento(self) -> None:
        self._listar_arquivos()
        self._ler_imagens()


    def _listar_arquivos(self) -> None:
        for p, _, files in os.walk(os.path.abspath(self.caminho_entradas)):
            for file in files:
                self.arquivos.append(file)


    def _ler_imagens(self) -> None:
        for nome_imagem_com_extensao in self.arquivos:
            self._montar_entradas(nome_imagem_com_extensao)
            self._montar_saidas(nome_imagem_com_extensao)


    def _montar_entradas(self, nome_imagem_com_extensao) -> None:
        entrada = Imagem(self.caminho_entradas+str(nome_imagem_com_extensao)).array()
        self.entradas.append(entrada)


    def _montar_saidas(self, nome_imagem_com_extensao) -> None:
        saida_numero = []
        nome = str(nome_imagem_com_extensao).replace('.png', '')
        caracter_entrada, _ = nome.split('_')
        binario = self._caracter_entrada_para_binario(caracter_entrada)
        for bit in binario:
            saida_numero.append(int(bit))
        self.saidas.append(saida_numero)


    def _caracter_entrada_para_binario(self, caracter) -> str:
        return str(format(ord(str(caracter)), '07b'))
