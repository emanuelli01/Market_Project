#################################################
# Acesso PostgreSQL e Criação do Banco de dados #
#################################################

# Acesse o postgres via PgAdmin, PSQL ou outro porgrama de sua escolha.

# Utilizando PgAdmin:
# Acesse o diretorio de instalação do PostgrSQL e utilize a interface 
# grafica para definir um nome de usuario, senha e os privilegios 
# necessarios. Como nao e recomendado utilizar o usuario de senha 
# de administador o recomendado é criar uma regra/usuario no postgres.
# defina um nome intuitivo como nome_do_projeto_que_voce_escolher_user
# e nome_do_projeto_que_voce_escolher_db.

# Criando um usuario para o banco de dados.

Servers >> PostgreSQL 13 >> Botão direito mouse >> create >> Login/Group Role

# Cria um banco de dados.

Servers >> PostgreSQL 13 >> Databases >> botao direito mouse >> create

# Vincule o usuario ao banco dea dados criado.

nome_do_projeto_que_voce_escolher_db >> Properties >> Security

# Utilizando PgSQL:
# Utilize linha de comandos e encontre o executavel no diretorio de
# instalação do PostgreSQL. Essas operações podem mudar dependendo 
# da versão ou do sistema operacional. Consulte os manuais e se 
# adapte ao ambiente instalado caso necessario.

psql (SQL Shell)

# O sistema solicitara as informações do banco uma de cada vez, 
# mas como elas não exitem aimda, voce somente precisa inserir 
# a informação de senha que sera para o usuario padrao "postgres"
# criado na instalacao do PostgreSQL (Caso tenha seguido as 
# orientacoes a sugestao de senha sera "123456". 

Server [localhost]: 
Database [postgres]: 
Port [5432]: 
Username [postgres]: 
Password for user postgres: 

# Como não e recomendado utilizar o usuario de senha de administador
# o recomendado e criar uma regra/usuario no postgres.

create role nome_de_usuairo_de_acesso_ao_banco with login password '123456';

# Crair um banco de dados no postgres

create database nome_banco_de_dados owner nome_de_usuairo_de_acesso_ao_banco;

# A seguir alguns comandos Postgres para verificar se o banco
# foi criado corretamente.

# Comando listar bancos de dados

\l

# Conectar a um banco de dados

\c nome_banco_de_dados

# Listar tabelas

\dt

# Listar colunas da tabela

\d nome_tabela


#######################################################
# As etapas a seguir devem ser executadas dentro      #
# do ambiente virtual de desenvolvimento do miniconda #
# para cada projeto. Ou seja com o conda atividado    #
# como por exemplo "(modeloapp) Antonio:~ antonio$"	  #
#######################################################

#########################################################
#### Raiz de projetos e Gerenciador Framework Django ####
#########################################################

# Acesse o diretorio de seus projetos e crie um projeto Framework Django

django-admin startproject nome_do_projeto_que_voce_escolher

# Observe a raiz do diretorio craido a partir do comando e 
# arvore de diretorios criada para o projeto basico do Django.

  (RAIZ)nome_do_projeto_que_voce_escolher
      .   
      ├── manage.py
      └── nome_do_projeto_que_voce_escolher (CONFIGURAÇÕES GERAIS)
          ├── __init__.py
          ├── asgi.py
          ├── settings.py
          ├── urls.py
          └── wsgi.py

# Caso ocorra algum problema de caminho nao encontrado, utilize
# o comando a seguir e tente novamente o comando django de de cricao
# de projeto "django-admin startproject nome_do_projeto_que_voce_escolher".

python -m django

# Inicializar o servico (Dependendo do servico sistema o comando pode mudar ".\manage.py runserver").

.\manage.py runserver

# Após o comando "manage.py runserver" o django criar um diretorio de 
# cache e um banco de dados nativo local "db.sqlite". O cache sao os
# logs e o banco sqlite nao sera utilizado por ser local e a melhor
# alternativa sempre sera banco de dados distribuidos ou em servidores.

  (RAIZ)nome_do_projeto_que_voce_escolher
      .
      ├── nome_do_projeto_que_voce_escolher
      │   ├── __init__.py
      │   ├── __pycache__
      │   │   ├── __init__.cpython-39.pyc
      │   │   ├── settings.cpython-39.pyc
      │   │   ├── urls.cpython-39.pyc
      │   │   └── wsgi.cpython-39.pyc
      │   ├── asgi.py
      │   ├── settings.py
      │   ├── urls.py
      │   └── wsgi.py
      ├── db.sqlite3
      └── manage.py
 
# Atraves do arquivo "manage.py" que as operacoes do Django so gerenciadas,
# por exemplo o comando de inicializar serviCo do socket do protocolo
# dere de http "./manage.py runserver".


############################################
# Desenvolvimento do projeto no IDE VSCode #
############################################

# Abrir VSCode.

# Open Folder e procurar o projeto RAIZ em seu computador e abrir.

  (RAIZ)nome_do_projeto_que_voce_escolher
      .
      ├── nome_do_projeto_que_voce_escolher
      │   ├── __init__.py
      │   ├── __pycache__
      │   │   ├── __init__.cpython-39.pyc
      │   │   ├── settings.cpython-39.pyc
      │   │   ├── urls.cpython-39.pyc
      │   │   └── wsgi.cpython-39.pyc
      │   ├── asgi.py
      │   ├── settings.py
      │   ├── urls.py
      │   └── wsgi.py
      ├── db.sqlite3
      └── manage.py


#######################
# Arquivo settings.py #
#######################

# O arquivo settings.py do Django e o local responsavel por todas
# as configuracoes gerais do framework django e suas declaracoes de 
# caminhos do sistemas para o desenvolvimento do software.

######################################################
# Configurações gerais do Django e do banco de dados #
######################################################

# No VSCode abra o arquivo de configurações do Django "settings.py".

# No "settings.py" no inicio do arquivo importar a modulo "OS" antes 
# do "from pathlib import Path". Serve para manipular funcionalidades
# do sistema operacional.

import os

# No "settings.py" no inicio do arquivo importar modulo "SYS" apos 
# "import os". Fornece funcoes e variaveis ​​usadas para manipular 
# partes do ambiente de tempo de execucao do Python.

import sys 

# No "settings.py" procure pela linha "from pathlib import Path" e 
# apos digite a linha a seguir para importar a biblioteca "decouple" 
# que server para esconder os dados de conexao do postgres garantindo 
# a seguranca.

from decouple import config

# No "settings.py" procure pela linha "BASE_DIR". Essa alteracao 
# muda o caminho do path dos diretorios de acesso do django.

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# No "settings.py" procure pela linha "SECRET_KEY" copie a chave de 
# seguranca que esta entre aspas e salve em um lugar seguro (Nao perca 
# a chave em hipotese alguma). Apos guardar a chave aleatorio substitua
# a linha pela seguinte descricao. Esse processo garantiara a seguranca
# do projeto.

SECRET_KEY = config('SECRET_KEY')

# No "settings.py" procure pela linha "DEBUG" e substitua a linha pela
# seguinte descricao. Esse procedimento tambem sera passado para um
# arquivo que ficara oculto.

DEBUG = config('DEBUG', default=False, cast=bool)

# "No "settings.py" procure pela linha DATABASES onde encontrara as 
# configurações do sqlite3, banco de dados local nativo do Djando. 
# Todo o conteudo devera ser substituido pelas seguintes informacoes
# de forma que os dados de acesso serao colocados em um arquivo de 
# CONFIG oculto assim como os dados do SECRET_KEY e DEBUG.

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),    
        'PORT': config('DB_PORT'),     
    }
}

# Esses procedimentos permitiram esconder as informacoes 
# importantes de seguranca. Agora para finalizar vamos criar
# esse arquivo de configuracao.
# Criar um arquivo no o nome especifico de ".env" na raiz do 
# projeto "(RAIZ)nome_do_projeto_que_voce_escolher" e inserir 
# as informacoes a seguir e salvar.

SECRET_KEY=Copiar a chave aleatoria salva e cole aqui sem aspas
DEBUG=True
DB_NAME=nome_de_usuairo_de_acesso_ao_banco
DB_USER=nome_banco_de_dados
DB_PASSWORD=123456
DB_HOST=localhost
DB_PORT=5432


#############################################################
##### Migracoes e Geracao de entidades no banco de dados ####
#############################################################

# Django Framework trabalha com Mapeamento Objeto-Relacional(ORM) 
# para percistencia de dados e migra as aplicacões existentes do 
# Django atraves das classes dos objetos criados gerando o banco 
# de dados baseado nessa estrutura.

# Comando de migracao necessario apos alteracoes nos objetos sao:
# "makemigrations" e "migrate".

./manage.py migrate

# Criar um usuario dentro da aplicacao do admin do Django.

./manage.py createsuperuser

# Defina o nome de usuario "admin", um email e senha valida
# sugestao "123456" e confirmar.

# Acessar o admin com os usuario e senha criados.

locahost:8000/admin

# Se tudo estiver correto ele acessara a implementação de adminstrador
# em inglês que já vem junto do Django.


##############################
# settings.py  Configuracoes #
##############################

# No "settings.py" procure pela linha "LANGUAGE_CODE" altere o conteúdo
# de lingua "en-us" para "pt-br". Pare o serviço do Djando, inicie 
# novamente e atualize a pagina de forma que as informacoes do Admin
# ficarao em portugues.

# Crie uma pasta "apps" na raiz do projeto.
# Acesse o arquivo "settings.py" e procure por BASE_DIR e 
# adicione as linhas seguintes para registrar os caminhos 
# onde os APPs ficarao, o django trabalha com APPs e para 
# cada entidade são criados APPs e seus objetos dentro de 
# sua composicao.

APPS_DIR = os.path.join(BASE_DIR, 'apps') 

sys.path.insert(0, APPS_DIR) 


##########################################################
# Configuracoes de diretorios e referencias do Front-end #
##########################################################

# Acesse o arquivo "settings.py", procure por STATIC_URL e logo apos
# adicione a linha seguir depois de STATIC_URL = '/static/' para referenciar
#  e adicionar o projeto para as pastas criadas onde ficarao os 
# arquivos estaticos do projeto, tais
# como as estruturas do front-end (CSS, JavaScript e Imagens).

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Logo a seguir adicione as linha para referenciar o 
# staticfiles para o registro dos arquivos estaticos.

STATICFILES_DIRS = [ 
    os.path.join(BASE_DIR, 'staticfiles'), 
]

# Na raiz do projeto crie a pasta "staticfiles" . Dentro 
# dessa pasta crie as pastas distintas "js", "css" e 'img'.

# Procurar por TEMPLATES e em seguida procure pelo campo DIRS e adicione
# nos colchetes na seguinte linha.

os.path.join(BASE_DIR, 'templates')

# Crie uma pasta "templates" na raiz do projeto para armazenar a 
# estrutura do front-end hibrido back-end com html e tags Django.

########
# URLS #
########

# Na raiz do projeto acesse o arquivo "urls.py". Nesse local serao declaradas as urls
# geral de cada App. Adicionar no import "from django.urls import path, include" o "include" de 
# forma que a importacao fica da seguinte forma.

from django.urls import path, include


#########################
#  Internationalization #
#########################

# Acesse o arquivo "settings.py", procure por LANGUAGE_CODE = 'en-usr'
# e altere para seguinte forma, assim todos os dados e configuracoes ficarao
# no formato portugues.

LANGUAGE_CODE = 'pt-br'





