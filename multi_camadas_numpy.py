import numpy as np

class Rede:
    def __init__(self):
        self.entradas = [[0,0], [0,1], [1,0], [1,1]]
        self.saidas   = [[0], [1], [1], [0]]
        self.pesos_camada_oculta = [
            [-0.424, -0.740, -0.961],
            [-0.358, -0.577, -0.469]]
        self.pesos_camada_saida = [
            [-0.017], [-0.893], [0.148]]

        self.qtd_neuronio_camada_oculta = 3
        self.camada_oculta = [[], [], [], []]
        self.resultados    = [[], [], [], []]
        self.apredizagem   = 0.1

        self.calcular()


    def calcular(self):
        soma_sinapse_oculta = np.dot(self.entradas, self.pesos_camada_oculta)
        camada_oculta       = self.ativacao(soma_sinapse_oculta)
        soma_sinapse_saida  = np.dot(camada_oculta, self.pesos_camada_saida)
        camada_saida        = self.ativacao(soma_sinapse_saida)
        erro_camada_saida   = self.calcular_valor_erro(self.saidas, camada_saida)
        media_absoluta      = self.media_absoluta_erro(erro_camada_saida)
        print(media_absoluta)
        print(erro_camada_saida)


    def ativacao(self, soma) -> float:
        # sigmoid function
        return 1 / ( 1 + np.exp(-soma) )


    def calcular_valor_erro(self, valor_esperado, resposta_obtida) -> float:
        return valor_esperado - resposta_obtida

    
    def media_absoluta_erro(self, erro_camada_saida):
        return np.mean(np.abs(erro_camada_saida))


Rede()