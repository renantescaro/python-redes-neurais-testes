from abc import ABC, abstractmethod
from typing import Any


class AtivacaoContract(ABC):
    @abstractmethod
    def ativar(self, valor: Any) -> Any:
        raise NotImplementedError()


    @abstractmethod
    def derivar(self, valor: Any) -> Any:
        raise NotImplementedError()

    @abstractmethod
    def __str__(self) -> str:
        raise NotImplementedError()
