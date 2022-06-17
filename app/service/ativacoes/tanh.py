from typing import Any
import numpy as np
from .ativacao_contract import AtivacaoContract


class Tanh(AtivacaoContract):
    """
        Função de avivação de -1 até 1
    """

    def ativar(self, valor: Any) -> Any:
        return np.tanh(valor)


    def derivar(self, valor: Any) -> Any:
        return 1.0 - np.tanh(valor)**2


    def __str__(self) -> str:
        return 'tanh'
