from PIL import Image
from PIL.Image import Image as ImageType
import numpy as np


class Imagem:
    def __init__(self) -> None:
        self.data = None
        self.type = None
        self.shape = None


    def _abrir_imagem(self, caminho_arquivo:str) -> bool:
        try:
            imagem:ImageType = Image.open(caminho_arquivo)
            self.data = np.array(imagem.convert('L'))
            self.type = type(self.data)
            self.shape = self.data.shape
            return True
        except Exception:
            return False


    def converter_np_array(self, caminho_arquivo:str):
        total = np.array([])
        if self._abrir_imagem(caminho_arquivo):
            for linha in self.data:
                total = np.append(total, linha)
        return total
