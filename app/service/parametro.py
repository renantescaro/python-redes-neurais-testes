import os
import numpy as np
from typing import Any, List, Optional, Tuple
from numpy import typing as np_type
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
        imagem_unica: str = ''
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
        self.imagem_unica = imagem_unica


    def _listar_arquivos(self) -> None:
        for _, _, files in os.walk(os.path.abspath(self.caminho_entradas)):
            self.arquivos.extend(iter(files))
            # for file in files:
            #     self.arquivos.append(file)


    def _ler_imagens(self) -> None:
        tamanho_nome_img = None
        for nome_imagem_com_extensao in self.arquivos:

            if tamanho_nome_img is None:
                tamanho_nome_img = len(nome_imagem_com_extensao)
            elif len(nome_imagem_com_extensao) != tamanho_nome_img:
                raise ValueError(
                    f'Nome da imagem com tamanho diferente! {nome_imagem_com_extensao}'
                )

            self._montar_entradas(nome_imagem_com_extensao)
            self._montar_saidas(nome_imagem_com_extensao)


    def _montar_entradas(self, nome_imagem_com_extensao:str) -> None:
        entrada = self.imagem.converter_np_array(
            caminho_arquivo=f'{self.caminho_entradas}{nome_imagem_com_extensao}'
        )
        self.entradas.append(entrada)


    def _montar_saidas(self, nome_imagem_com_extensao:str) -> None:
        nome_imagem = nome_imagem_com_extensao.replace('.png', '')

        # imagem com 1 caracter
        if '_' in nome_imagem:
            caracter_entrada, _ = nome_imagem.split('_')
            binario = self._caracter_para_binario(caracter_entrada)
            saida_numero = self._binario_para_lista_inteiros(binario)

        # imagem com mais de 1 caracter
        else:
            saida_numero = np.array([])
            for caracter in nome_imagem:
                binario = self._caracter_para_binario(caracter)
                saida_atual = self._binario_para_lista_inteiros(binario)
                saida_numero = np.concatenate((saida_numero, np.array(saida_atual)))

        self.saidas.append(saida_numero)


    def _binario_para_lista_inteiros(self, binario:str) -> Optional[List[int]]:
        """
            recebe binario e converte para lista de inteiros
            conforme a função de ativação utilizada
        """
        if str(self.ativacao) == 'sigmoid':
            return [int(bit) for bit in binario]

        if str(self.ativacao) == 'tanh':
            return [-1 if int(bit) == 0 else 1 for bit in binario]


    def _caracter_para_binario(self, caracter:str) -> str:
        """
            converte número ou caracter recebido em binário
        """
        try:
            convertido = int(caracter)
        except ValueError:
            convertido = ord(caracter)

        return format(convertido, '08b')


    def executar_prod(self) -> List[np_type.NDArray[Any]]:
        entrada = self.imagem.converter_np_array(
            caminho_arquivo=f'{self.imagem_unica}'
        )
        self.entradas.append(entrada)
        return self.entradas


    def executar(self) -> Tuple[
        List[np_type.NDArray[Any]],
        List[List[Any]]
    ]:

        self._listar_arquivos()
        self._ler_imagens()
        return self.entradas, self.saidas
