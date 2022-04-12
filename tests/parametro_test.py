import numpy as np
import sys
sys.path.append('C:\_python_pessoal\python-redes-neurais-testes')
from classes.parametro import Parametro


# 0 -> 0, 1, 1, 0, 0, 0, 0
# 1 -> 0, 1, 1, 0, 0, 0, 1
# 2 -> 0, 1, 1, 0, 0, 1, 0
# 3 -> 0, 1, 1, 0, 0, 1, 1
# 4 -> 0, 1, 1, 0, 1, 0, 0
# 5 -> 0, 1, 1, 0, 1, 0, 1
# 6 -> 0, 1, 1, 0, 1, 1, 0
# 7 -> 0, 1, 1, 0, 1, 1, 1
# 8 -> 0, 1, 1, 1, 0, 0, 0
# 9 -> 0, 1, 1, 1, 0, 0, 1

parametro = Parametro()
parametro._montar_saidas('9_1.png')

print(parametro.saidas)
