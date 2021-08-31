import os


class Entrada:
    def __init__(self):
        self.arquivos = []
        self.caminho_entradas = 'assets/treinamento'


    def listar_arquivos(self):
        for p, _, files in os.walk(os.path.abspath(self.caminho_entradas)):
            for file in files:
                self.arquivos.append(file)


    def ler_imagens(self):
        for imagem in self.arquivos:
            nome = str(imagem).replace('.png', '')
            print(nome.split('_'))


    def teste(self):
        self.listar_arquivos()
        self.ler_imagens()


Entrada().teste()