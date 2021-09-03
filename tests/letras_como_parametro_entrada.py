import numpy as np
import sys
sys.path.append('C:/Users/renan.tescaro/Desktop/python/python-redes-neurais-testes/')
from classes.parametro import Parametro


parametro = Parametro()
parametro.caminho_entradas = 'assets/treinamento_letras/'
parametro.carregar_assets_treinamento()
saidas = parametro.saidas

for s in saidas:
    print(s)