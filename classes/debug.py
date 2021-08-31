import os.path
from datetime import datetime as dt


class Debug:
    def __init__(self, texto, nome_arquivo='debug'):
        # debug a data atual no nome
        data    = self._data_atual_string_txt()
        arquivo = 'debug/'+str(nome_arquivo)+str('-')+str(data)+'.txt'

        # verifica se debug já existe
        f = None
        if os.path.exists(arquivo):
            f = open(arquivo, 'a')
        else:
            f = open(arquivo, 'w')

        # conteudo a gravar no debug
        conteudo = self._data_atual_string() + ': ' + str(texto) +'\n'

        # grava conteudo e fecha arquivo
        f.write(conteudo)
        f.close()


    def _data_atual_string(self):
        data_hoje = dt.today()
        return str(data_hoje.strftime('%d/%m/%Y %H:%M:%S'))


    def _data_atual_string_txt(self):
        data_hoje = dt.today()
        return str(data_hoje.strftime('%d-%m-%Y'))