import cv2
import numpy as np
from PIL import Image, ImageOps
from PIL.Image import Image as ImageType
from cv2 import Mat as cv2ImageType


class Binarizacao:

    @staticmethod
    def executar(imagem, limiar:int, nome_imagem:str) -> cv2ImageType:
        imagem = Image.fromarray(cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB))
        rgb_imagem = imagem.convert('RGB')
        linha = np.size(imagem, 0)
        coluna = np.size(imagem, 1)
        img_final = Image.new('RGB', (coluna, linha))

        qtd_vermelho = 0
        qtd_azul = 0
        qtd_verde = 0

        # linha
        for i in range(linha):
            # coluna
            for j in range(coluna):
                r, g, b = rgb_imagem.getpixel((j, i))

                qtd_vermelho += 1 if int(r) > 200 else 0
                qtd_azul += 1 if int(b) > 200 else 0
                qtd_verde += 1 if int(g) > 200 else 0

                cor = 255 if int(b) > limiar else 0
                img_final.putpixel((j, i), (cor, cor, cor))

        # if nome_imagem in ['91.png', '100.png', '105.png']:
        #     print(nome_imagem, qtd_vermelho, qtd_azul, qtd_verde)

        # qtd de pixel 98100
        if qtd_vermelho > 70000:
            # print(f'{nome_imagem} inverte!')
            img_final = ImageOps.invert(img_final)

        return cv2.cvtColor(np.asarray(img_final), cv2.COLOR_RGB2BGR)
