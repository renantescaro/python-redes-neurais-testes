import numpy as np

def sigmoid(soma):
    return 1 / (1 + np.exp(-soma))

def sigmoidDerivada(sig):
    return sig * (1 - sig)

entradas = np.array([
    [0,0],
    [0,1],
    [1,0],
    [1,1] ])

saidas = np.array([
    [0],
    [1],
    [1],
    [0] ])

pesos_camada_oculta = np.array([
    [-0.424, -0.740, -0.961],
    [0.358, -0.577, -0.469] ])
    
pesos_camada_saida = np.array([
    [-0.017], [-0.893], [0.148] ])

taxaAprendizagem = 0.3
momento          = 1
epocas           = 100000
resultado        = None

# Erro: 0.1331255301244873
# Pesos camada saida:
# [[0.01174907]
#  [0.98969039]
#  [0.98969064]
#  [0.50013409]]

for j in range(epocas):
    camadaEntrada = entradas
    soma_sinapse_oculta   = np.dot(camadaEntrada, pesos_camada_oculta)
    camada_oculta_ativada = sigmoid(soma_sinapse_oculta)
    soma_sinapse_saida    = np.dot(camada_oculta_ativada, pesos_camada_saida)
    camada_saida_ativada  = sigmoid(soma_sinapse_saida)
    resultado             = camada_saida_ativada

    erroCamadaSaida = saidas - camada_saida_ativada
    mediaAbsoluta = np.mean(np.abs(erroCamadaSaida))
    print("Erro: " + str(mediaAbsoluta))

    # calcula Deltas
    deltaSaida  = erroCamadaSaida * sigmoidDerivada(camada_saida_ativada)
    deltaOculta = (deltaSaida.dot(pesos_camada_saida.T)) * (sigmoidDerivada(camada_oculta_ativada))

    # calcula novos pesos da camada de saida
    pesos_saida_novos  = camada_oculta_ativada.T.dot(deltaSaida)
    pesos_camada_saida = (pesos_camada_saida * momento) + (pesos_saida_novos * taxaAprendizagem)

    # calcula novos pesos da camada oculta
    pesos_oculta_novos  = camadaEntrada.T.dot(deltaOculta)
    pesos_camada_oculta = (pesos_camada_oculta * momento) + (pesos_oculta_novos * taxaAprendizagem)
    
    
print(resultado)