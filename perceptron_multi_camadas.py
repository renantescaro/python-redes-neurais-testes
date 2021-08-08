import numpy as np

class Rede:
    def __init__(self):
        self.entradas = np.array(
            [[0,0], [0,1], [1,0], [1,1]] )

        self.saidas = np.array(
            [[0], [1], [1], [0]])

        self.pesos_camada_oculta = np.array([
            [-0.424, -0.740, -0.961],
            [-0.358, -0.577, -0.469]] )

        self.pesos_camada_saida = np.array([
            [-0.017], [-0.893], [0.148]] )

        self.qtd_neuronio_camada_oculta = 3
        self.camada_oculta = np.array([[], [], [], []])
        self.resultados    = np.array([[], [], [], []])
        self.apredizagem   = 0.3
        self.momento       = 1

        self.calcular()


    def calcular(self):
        soma_sinapse_oculta   = np.dot(self.entradas, self.pesos_camada_oculta)
        camada_oculta_ativada = self.ativacao(soma_sinapse_oculta)
        soma_sinapse_saida    = np.dot(camada_oculta_ativada, self.pesos_camada_saida)
        camada_saida_ativada  = self.ativacao(soma_sinapse_saida)

        # calculo do erro
        erro_camada_saida = self.calcular_valor_erro(self.saidas, camada_saida_ativada)
        media_absoluta    = self.media_absoluta_erro(erro_camada_saida)

        # calcula Deltas
        delta_saida  = erro_camada_saida * self.derivada_ativacao(camada_saida_ativada)
        delta_oculta = delta_saida.dot(self.pesos_camada_saida.T) * self.derivada_ativacao(camada_oculta_ativada)

        # calcula novos pesos
        pesos_saida_novos       = camada_oculta_ativada.T.dot(delta_saida)
        self.pesos_camada_saida = (self.pesos_camada_saida * self.momento) + (pesos_saida_novos * self.apredizagem)

        print('\n ------------------------ \n ')
        print('Pesos camada saida ' + str(self.pesos_camada_saida)+'\n')
        print('Media absoluta ' + str(media_absoluta)+'\n')
        print('Erro camada saida ' + str(erro_camada_saida)+'\n')
        print(' ------------------------ \n')

    def ativacao(self, soma) -> float:
        return self.sigmoid_function(soma)


    def sigmoid_function(self, soma) -> float:
        return 1 / ( 1 + np.exp(-soma) )


    # utilizada para indicar a direção dos pesos
    # no grafico de gradientes
    def derivada_ativacao(self, valor_ativacao):
        return valor_ativacao * (1 - valor_ativacao)


    def delta_saida(self, erro_camada_saida, derivada_saida):
        return erro_camada_saida * derivada_saida


    def delta_oculta(self, derivada, peso, delta_saida):
        return derivada * peso * delta_saida


    def calcular_valor_erro(self, valor_esperado, resposta_obtida) -> float:
        return valor_esperado - resposta_obtida

    
    def media_absoluta_erro(self, erro_camada_saida):
        return np.mean(np.abs(erro_camada_saida))


Rede()