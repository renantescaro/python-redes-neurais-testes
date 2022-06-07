from typing import Any
import numpy as np
from .ativacao_contract import AtivacaoContract


class Sigmoid(AtivacaoContract):
    def ativar(self, valor: Any) -> Any:
        return 1 / ( 1 + np.exp(-valor) )


    def derivar(self, valor: Any) -> Any:
        return valor * (1 - valor)
