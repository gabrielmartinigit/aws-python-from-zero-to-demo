# Módulo 2 - Criando uma API com Flask

[Flask](https://flask.palletsprojects.com/en/2.2.x/quickstart/) é um micro framework que utiliza a linguagem Python para criar aplicativos Web.

## Preparando o ambiente

```bash
pip install virtualenv
virtualenv .venv
source .venv/bin/activate
pip install Flask
python app.py
```

## Roteamento

```python
@app.route('/')
def index():
    return 'Index'

@app.route('/hello')
def hello():
    return 'Olá Mundo!'
```

## Variáveis

```python
@app.route('/user/<username>')
def show_user_profile(username):
    return f'Usuário {username}'
```

## Métodos HTTP

```python
# GET
@app.get('/cats')
def get_cats():
    return ['Abobrinha', 'Vilma']

@app.route('/cats', methods=['GET'])
def get_cats():
    return ['Abobrinha', 'Vilma']

# Query String
from flask import request

@app.get('/cats')
def get_cats():
    args = request.args
    gato = args.get('gato')
    return f'Nome é: {gato}'

# POST
@app.post('/cats')
def post_cats():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.json
        return json
    else:
        return 'Content-Type not supported!'
```

## Testando a API

```bash
curl -X GET "localhost:5000"
curl -X POST -H "Content-type: application/json" -d "{\"Gato\" : \"Abobrinhha\"}" "localhost:5000/cats"
```

## Desafios

1. Crie uma API com método GET que recebe o nome e a língua do usuário e retorna um conselho do dia.
