import numpy as np

class Rede:
    def __init__(self):
        self.entradas = [[0,0], [0,1], [1,0], [1,1]]
        self.saidas   = [0, 1, 1, 0]
        self.pesos    = [-0.424, 0.358, -0.740,
                        -0.577, -0.961, -0.469]

        self.qtd_neuronio_camada_oculta = 3
        self.camada_oculta = [[], [], [], []]
        self.resultados    = [[], [], [], []]
        self.apredizagem   = 0.1

        self.calcular()
        self.imprimir_resultado_oculta()
        # self.recalcular_pesos()


    def calcular(self):
        # loop pelos grupos de entrada
        posi_oculta = 0
        for entrada in self.entradas:

            # calculo por camada
            posi_peso = 0
            for camada in range(self.qtd_neuronio_camada_oculta):

                # função de soma
                soma = 0
                for e in entrada:
                    soma += e * self.pesos[posi_peso]
                    posi_peso += 1

                # função de ativação
                status = self.ativacao(soma)

                # adiciona soma e status na camada oculta
                self.camada_oculta[posi_oculta].append(
                    {'soma'  : soma,
                    'status' : status} )
            posi_oculta += 1


    def calcular_valor_erro(self, valor_esperado, resposta_obtida) -> float:
        return abs(valor_esperado - resposta_obtida)


    def calcular_novo_peso(self, peso_atual, entrada, erro) -> float:
        return peso_atual + ( self.apredizagem * entrada * erro )


    def recalcular_pesos(self):
        for posi_entrada in range(len(self.entradas)):
            print('entradas: '+str(self.entradas[posi_entrada]))
            # verificar se houve erro
            # self.saidas[posi_entrada]
            # oculta['status']


    def imprimir_resultado_oculta(self):
        for posi_entrada in range(len(self.entradas)):
            print('entradas: '+str(self.entradas[posi_entrada]))
            for oculta in self.camada_oculta[posi_entrada]:
                print('soma: '+str(oculta['soma']) +
                     ' status: '+str(oculta['status'])+
                     ' saida: '+ str(self.saidas[posi_entrada]))
            print('---------')


    def ativacao(self, soma) -> float:
        # sigmoid function
        return 1 / ( 1 + np.exp(-soma) )


Rede()