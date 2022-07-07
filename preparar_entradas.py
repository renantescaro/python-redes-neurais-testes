from typing import List
import cv2
import os
from PIL import Image
from cv2 import Mat as cv2ImageType
from app.service.binarizacao import Binarizacao


limiar = 83
resolucao_corte = (545, 180)
caminho_origem = 'assets/treinamento/placas_originais'
caminho_destino = 'assets/treinamento/placas_binarizadas'
rect = cv2.getStructuringElement(cv2.MORPH_RECT, (8, 8))
elip = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7))


def listar_imagens() -> List:
    imagens_originais = []
    for _, _, nome_imagem in os.walk(os.path.abspath(caminho_origem)):
        imagens_originais.extend(iter(nome_imagem))
    return imagens_originais


for nome_imagem in listar_imagens():
    imagem = cv2.imread(f'{caminho_origem}/{nome_imagem}')
    imagem = cv2.resize(imagem, resolucao_corte)

    if nome_imagem in ['15.png', '20.png', '22.png', '34.png']:
        imagem = cv2.erode(imagem, rect, iterations=1)
        imagem = cv2.dilate(imagem, elip, iterations=2)

    imagem = Binarizacao.executar(imagem, limiar, nome_imagem)

    cv2.imwrite(f'{caminho_destino}/{nome_imagem}', imagem)
