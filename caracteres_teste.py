from PIL import Image

# LLLNLNN

imagem = Image.open('0.png')
colunas, linhas = imagem.size
entradas = [
    # 0
    [0,0,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,0,0,1],
    # 1
    [1,0,1,1,0,0,1,1,1,0,1,1,1,0,1,1,0,0,0,1],
]
entrada = []
saidas  = [
    # 0
    [0,0,0,0,0,0,0,0,0,0],
    # 1
    [0,1,0,0,0,0,0,0,0,0],
    # 2
    [0,0,1,0,0,0,0,0,0,0],
    # 3
    [0,0,0,1,0,0,0,0,0,0],
    # 4
    [0,0,0,0,1,0,0,0,0,0],
    # 5
    [0,0,0,0,0,1,0,0,0,0],
    # 6
    [0,0,0,0,0,0,1,0,0,0],
    # 7
    [0,0,0,0,0,0,0,1,0,0],
    # 8
    [0,0,0,0,0,0,0,0,1,0],
    # 9
    [0,0,0,0,0,0,0,0,0,1],
]

# linha
for i in range(linhas):
    # coluna
    for j in range(colunas):
        rgb_imagem = imagem.convert('RGB')
        _, _, b = rgb_imagem.getpixel((j, i))
        if b > 100:
            entrada.append(1)
        else:
            entrada.append(0)
print(entrada)