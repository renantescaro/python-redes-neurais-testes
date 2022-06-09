from typing import Any
import numpy as np
from .ativacao_contract import AtivacaoContract


class Tanh(AtivacaoContract):
    """
        Função de avivação de -1 até 1
    """

    def ativar(self, valor: Any) -> Any:
        return (np.exp(valor) - np.exp(-valor)) / (np.exp(valor) + np.exp(-valor))


    def derivar(self, valor: Any) -> Any:
        return 1 - self.ativar(valor) * self.ativar(valor)


    def __str__(self) -> str:
        return 'tanh'
