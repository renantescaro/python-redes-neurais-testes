from typing import Any
import numpy as np
from .ativacao_contract import AtivacaoContract


class Sigmoid(AtivacaoContract):
    """
        Função de avivação de 0 até 1
    """

    def ativar(self, valor: Any) -> Any:
        return 1 / ( 1 + np.exp(-valor) )


    def derivar(self, valor: Any) -> Any:
        return valor * (1 - valor)


    def __str__(self) -> str:
        return 'sigmoid'
