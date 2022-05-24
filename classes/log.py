import os.path
from datetime import datetime as dt


class Log:
    @staticmethod
    def info(texto:str, nome_arquivo='log') -> None:
        data    = Log._data_atual_string_txt()
        arquivo = f'log/{nome_arquivo}-{data}.log'

        f = None
        f = open(arquivo, 'a') if os.path.exists(arquivo) else open(arquivo, 'w')
        conteudo = f'{Log._data_atual_string()} {texto}\n'

        f.write(conteudo)
        f.close()


    @staticmethod
    def _data_atual_string() -> str:
        return str(dt.now().strftime('%d/%m/%Y %H:%M:%S'))


    @staticmethod
    def _data_atual_string_txt() -> str:
        return str(dt.now().strftime('%d-%m-%Y'))
