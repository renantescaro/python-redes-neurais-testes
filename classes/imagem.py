from PIL import Image
import numpy as np


class Imagem:
    def __init__(self, caminho_arquivo):
        imagem     = Image.open(caminho_arquivo)
        self.data  = np.array(imagem.convert('L'))
        self.type  = type(self.data)
        self.shape = self.data.shape

    
    def array(self):
        total = np.array([])
        for linha in self.data:
            total = np.append(total, linha)
        return total