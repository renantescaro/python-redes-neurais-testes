from datetime import datetime
from pytz import timezone


class Datas:
    @staticmethod
    def data_hora_atual():
        data_e_hora_atuais = datetime.now()
        fuso_horario = timezone('America/Sao_Paulo')
        return data_e_hora_atuais.astimezone(fuso_horario)
