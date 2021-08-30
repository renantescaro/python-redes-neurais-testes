from perceptron_multi_camadas import PerceptronMultiCamadas
from imagem import Imagem

foto_numero = Imagem('1.png')
# print(foto_numero.data)

# qtd = 1
# for linha in foto_numero.data:
#     print(str(qtd)+': '+str(linha))
#     qtd +=1


PerceptronMultiCamadas(
    entradas = foto_numero.data,
    saidas   = []
).calcular()