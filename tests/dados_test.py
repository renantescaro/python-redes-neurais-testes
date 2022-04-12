import sys
sys.path.append('C:\_python_pessoal\python-redes-neurais-testes')
from classes.dados import Dados
import pickle


# Dados('entradas', [12, 98, 465, 43, 32, 45, 2])

banco = Dados()

#banco.set('pesos_camada_saidaa', 'efe ewf we')

pesos_camada_saida = banco.get('pesos_camada_saida')
print(pesos_camada_saida)
