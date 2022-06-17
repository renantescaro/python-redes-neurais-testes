from typing import Any
import numpy as np
from .ativacao_contract import AtivacaoContract


class LeakyRelu(AtivacaoContract):
    """
        Função de avivação de -0.5 até +
    """

    def ativar(self, valor: Any) -> Any:
        data = [max(0.05*value, value) for value in valor]
        return np.array(data, dtype=float)


    def derivar(self, valor: Any) -> Any:
        data = [1 if value>0 else 0.05 for value in valor]
        return np.array(data, dtype=float)


    def __str__(self) -> str:
        return 'leaky_relu'
