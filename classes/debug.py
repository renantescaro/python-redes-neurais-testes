import os.path
from datetime import datetime as dt


class Debug:
    def __init__(self, texto, nome_arquivo='debug') -> None:
        # debug a data atual no nome
        data    = self._data_atual_string_txt()
        arquivo = f'debug/{nome_arquivo}-{data}.txt'

        # verifica se debug já existe
        f = None
        f = open(arquivo, 'a') if os.path.exists(arquivo) else open(arquivo, 'w')
        # conteudo a gravar no debug
        conteudo = f'{self._data_atual_string()}:{texto}\n'

        # grava conteudo e fecha arquivo
        f.write(conteudo)
        f.close()


    def _data_atual_string(self) -> str:
        return str(dt.now().strftime('%d/%m/%Y %H:%M:%S'))


    def _data_atual_string_txt(self) -> str:
        return str(dt.now().strftime('%d-%m-%Y'))
