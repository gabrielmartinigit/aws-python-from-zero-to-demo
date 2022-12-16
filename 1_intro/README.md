# Módulo 1 - Introdução ao Python

## Conhecendo o Python

Python é uma linguagem de programação interpretada de alto nível e que suporta múltiplos paradigmas de programação: imperativo, orientado a objetos e funcional. É uma linguagem com tipagem dinâmica e gerenciamento automático de memória.

Execute o Python no seu terminal:

```bash
python --version
python
```

Finalize a execução do Python ao final do módulo:

```bash
quit()
```

## Variáveis e tipos

```python
# String
nome = 'Gabriel'
print('Olá Mundo ' + nome)
print(type(nome))

# Int
idade = 25
print(idade)
print(type(idade))

# Float
altura = 1.72
print(altura)
print(type(altura))

# Bool
tem_gatos = True
print(tem_gatos)
print(type(tem_gatos))

# Dictionary
usuario = {'nome':nome, 'idade':idade, 'altura':altura, 'tem_gatos':tem_gatos, 'cidade':'Guarulhos'}
print(f'Dados do usuário: {usuario}')
print(type(usuario))

# List
gatos = ['Abobrinha', 'Nelson', 'Vilma', 'Preta']
print(gatos)
print(gatos[0])
print(gatos[-1])
print(type(gatos))
print(type(gatos[0]))
```

## Condicional

```python
numero_1 = 10
numero_2 = 8

# se ... então ...
# operadores: ==, !=, >, <, >=, <=
if numero_1>numero_2:
    print(numero_1)

numero_2 = 18

# se ... senão ...
if numero_1>numero_2:
    print(numero_1)
else:
    print(numero_2)

numero_1 = numero_2

# se encadeado
if numero_1>numero_2:
    print(numero_1)
elif numero_1<numero_2:
    print(numero_2)
else:
    print('igual')
```

## Loops

```python
# para númerico
for number in range(10):
    print(number)

# para lista
cachorros = ['maria', 'espeto', 'bisteca']

for cachorro in cachorros:
    print(cachorro)

# para lista com índice
for index, cachorro in enumerate(cachorros):
    print(index, cachorro)

# enquanto
i=0
while i<len(cachorros):
    print(cachorros[i])
    i+=1
```

## Funções

```python
# função sem parâmetro
def hello_world():
    print('Olá mundo!')

hello_world()

# função vazia
def null_function():
    pass

numero_1 = 10
numero_2 = numero_1

# função com dois parâmetros
def soma(n1, n2):
    return n1+n2

# chamando a função com dois argumentos
soma(numero_1, numero_2)

# chamando a função com a chave do argumento
soma(n1=numero_1, n2=numero_2)

# valor padrão para o parâmetro
def soma_padrao(n2, n1=10):
    return n1+n2

soma_padrao(n2=1)

```

```bash
# a função main no Python é reservada para ser executada automaticamente no início do programa
python app.py
```

## Exceções

```python
# para tratar possíveis exceções, podemos encapsular nosso código com try except
while True:
    try:
        n1 = int(input('Entre um número: '))
    except Exception:
        print("Algo deu errado, tente novamente")

# trantando exceções específicas
while True:
    try:
        n1 = int(input('Entre um número: '))
    except ValueError:
        print("Digite um número")
    except Exception as err:
        print(f"Algo deu errado: {err}")
        raise
```

## Bibliotecas

```python
# bibliotecas nativas https://docs.python.org/3/library/
nome = 'Gabriel'

help(type(nome))
dir(nome)
print(nome.upper())

# importando uma biblioteca
import datetime

hoje = datetime.date.today()
print(hoje)

# renomeando uma classe importada
import datetime as data

print(data.date.today())

# importando apenas uma classe da biblioteca
from datetime import datetime

agora = datetime.now()
print(agora)
```

E quando temos que trabalhar com bibliotecas não nativas? O PIP é uma ferramenta para gerenciamento de pacotes escrito em Python. Serve para instalar, remover, atualizar ou listar os pacotes instalados em um determinado projeto.

```bash
# instalando o AWS SDK para Python https://boto3.amazonaws.com/v1/documentation/api/latest/index.html
pip install boto3
```

```python
import boto3

dir(boto3)
help(boto3.client)

boto3.session.Session().get_available_services()

translate_client = boto3.client('translate')

dir(translate_client)
help(translate_client.translate_text)

def traduzir_texto(texto):
    response = translate_client.translate_text(
        Text=texto,
        SourceLanguageCode='pt',
        TargetLanguageCode='en'
    )

    return response

texto = "Olá mundo!"

print(traduzir_texto(texto)['TranslatedText'])
```

```bash
# listando as bibliotecas utilizadas
pip freeze

# salvando as bibliotecas utilizadas em um arquivo
pip freeze > requirements.txt
```

## Ambiente Virtual

O virtualenv é uma ferramenta para criar ambientes isolados em Python.

```bash
# instalando o virtualenv
pip install virtualenv

# criando um ambiente virtual
virtualenv .venv

# iniciando um ambiente virtual
source .venv/bin/activate

# verificando as bibliotecas do ambiente
pip freeze

# instalando as dependências do projeto no ambiente
pip install -r requirements.txt
```

## Desafios

1. Crie um programa para pedir nome, idade e cidade e imprimir as informações.
2. Faça um programa que peça dois números e imprima o resto da divisão.
3. Faça um programa que peça um texto e a língua para tradução, crie uma função para traduzir e imprimir o texto na língua desejada.
4. Faça um programa para mostrar o conselho do dia (https://api.adviceslip.com/advice).
5. Crie um programa que recebe o nome e a língua do usuário, gere um conselho do dia e gere o áudio em mp3 do conselho na língua desejada.
