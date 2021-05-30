class Rede:
    def __init__(self):
        self.entradas    = [[0,0], [0,1], [1,0], [1,1]]
        self.saidas      = [0, 0, 0, 1]
        self.pesos       = [0.1, 0.1]
        self.resultado   = []
        self.apredizagem = 0.001
        self.sucesso     = False

        while not self.sucesso:
            self.calular()
            self.imprimir_resultado()
            print('-----------')
            self.recalcular_pesos()


    def calular(self):
        posi = 0
        for entrada in self.entradas:
            status_neuronio = self.calcular_saida(entrada)
            self.resultado.append(
                {
                    'posicao' : posi,
                    'status'  : status_neuronio,
                    'entrada' : entrada,
                    'saida'   : self.saidas[posi]
                } )
            posi += 1


    def imprimir_resultado(self):
        for r in self.resultado:
            print('posição: ' +str(r['posicao'])+
                  ' status: ' +str(r['status'])+
                  ' saida:  ' +str(r['saida'] )+
                  ' entrada: '+str(r['entrada'][0])+' e '+str(r['entrada'][1]) )
        for p in self.pesos:
            print('peso: '+str(p))


    def recalcular_pesos(self):
        self.sucesso = True
        for r in self.resultado:
            if r['status'] != r['saida']:
                self.resultado = []
                self.sucesso = False
                erro = self.calcular_valor_erro(
                    valor_esperado  = r['posicao'],
                    resposta_obtida = r['status'] )

                for p in range(len(self.pesos)):
                    self.pesos[p] = self.calcular_novo_peso(
                        entrada      = float(r['entrada'][p]),
                        peso_atual   = float(self.pesos[p]),
                        aprendizagem = float(self.apredizagem),
                        erro         = float(erro) )


    def somar(self, entradas, pesos) -> float:
        soma = 0
        for posi in range(len(entradas)):
            soma += entradas[posi] * pesos[posi]
        return float(soma)

    
    def calcular_saida(self, registro) -> bool:
        resultado_soma = self.somar(registro, self.pesos)
        return self.ativar(resultado_soma)


    def ativar(self, soma) -> bool:
        return 0 if soma < 1 else 1


    def calcular_valor_erro(self, valor_esperado, resposta_obtida) -> float:
        return valor_esperado - resposta_obtida


    def calcular_novo_peso(self, peso_atual, aprendizagem, entrada, erro) -> float:
        return peso_atual + ( aprendizagem * entrada * erro )


Rede()