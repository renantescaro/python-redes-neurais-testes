## Rede Neural Artificial
- Python 3.10.0

* Rede PMC (Perceptron Multicamadas), MLP (Multilayer perceptron) - semelhante a rede Perceptron de 1958, mas com mais de uma camada
* Correção dos pesos de 'modo padrão', a correção dos pesos é realizada a cada iteração e se baseia apenas na entrada atual
* Ativação por Sigmoid Function
* Treinamento por Backpropagation

<img src='assets/PMC_MLP.png' style="width: 600px">

<br><br>


## Estrutura de treinamento e execução de Rede Neural Artificial
* Arquivo 'executar_treinamento.py' é responsavel por treinar a rede.
* Na pasta '\assets\treinamento\' temos as subpastas com os elementos de treinamento da rede.
Usando a subpasta 'numeros_placas' como exemplo, note que os nomes das imagens segue um padrão, exemplo:
'0_1.png', onde o primeiro caracter é o caracter que esta na imagem, e após o underscore do nome, temos qual a sequência, que inicia no numero 1,
podendo ter diversas imagens para realizar o treinamento de um único caracter (0_1.png, 0_2.png, 0_3.png etc)
* Na pasta '\assets\pesos\' temos os .csv que armazenam os pesos da rede.
* Na pasta '\assets\graficos\' temos as possiveis plotagem de graficos utilizadas.

<br><br>

## Instalação das Dependências


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

<br>

### No Linux
1 - Instalar todas as dependências
```bash
python -m venv venv
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


<br><br>

## Criação de .env
* Deve ser criado arquivo .env na raiz do projeto, utilizar como referencia arquivo '.env-example'
* As seguintes variáveis são necessárias:
```env
DATABASE_URL = 'mysql://USUARIO_BANCO:SENHA_BANCO@IP/NOME_BANCO'
IP_APLICACAO = '0.0.0.0'
PORTA_APLICACAO = '80'
```


<br><br>

## Banco de Dados
* Foi utilizado banco de dados MySQL / MariaDB para gravação de log / resultados.
* Na raiz do projeto, arquivo 'assets/banco.sql' posssui a estrutura do banco.
* Não esqueça da string de conexão no arquivo '.env'

<br><br>

### Executar aplicação web
* Não esqueça das variáveis no arquivo '.env'
```bash
python run_web_app.py
```

### Executar aplicação web em modo dev
```bash
set FLASK_APP=app
set FLASK_ENV=development
set FLASK_RUN_HOST=0.0.0.0
set FLASK_RUN_PORT=80
flask run
```


<br><br>

### Testes Unitários
```bash
pytest --cov-config=.coveragerc --cov-report html --cov=. classes/
```
