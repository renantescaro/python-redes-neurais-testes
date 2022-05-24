### perceptron_multi_camadas.py
* Rede PMC (Perceptron Multicamadas), MLP (Multilayer perceptron) - semelhante a rede Perceptron de 1958, mas com mais de uma camada
* Correção dos pesos de 'modo padrão', a correção dos pesos é realizada a cada iteração e se baseia apenas na entrada atual
* Ativação por Sigmoid Function
* Treinamento por Backpropagation

<img src='assets/PMC_MLP.png'>

### No Windows
1 - Instalar todas as dependências
```bash
python -m venv venv
venv\Scripts\activate.bat
pip install -r requirements.txt
```

2 - Executar
```bash
venv\Scripts\activate.bat
python executar_treinamento.py
ou
python executar_rede.py
```

### No Linux
1 - Instalar todas as dependências
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

2 - Executar
```bash
source venv/bin/activate
python executar_treinamento.py
ou
python executar_rede.py
```
