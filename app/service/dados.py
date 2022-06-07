from typing import Any
from numpy import savetxt
from numpy import loadtxt


class Dados:
    def __init__(self, versao=None) -> None:
        self._caminho = 'assets/pesos/'
        self._tipo = '.csv'
        self.versao = versao


    def _caminho_arquivo(self, chave:str) -> str:
        if self.versao is None:
            return f'{self._caminho}{chave}{self._tipo}'
        return f'{self._caminho}{chave}_{self.versao}_{self._tipo}'


    def set(self, chave:str, valor:Any) -> None:
        arquivo = self._caminho_arquivo(chave)
        savetxt(arquivo, valor, delimiter=',')


    def get(self, chave:str) -> Any:
        arquivo = self._caminho_arquivo(chave)
        return loadtxt(arquivo, delimiter=',')
