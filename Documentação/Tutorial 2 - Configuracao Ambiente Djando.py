############################################
#                  MINICONDA               #
# Criacao de Ambiente virtual isolado para #
# instalacao das bibliotecas necessarias   #
# para o desenvolvimento do projeto        #
############################################

# Criar ambiente virtual de programacao novamente (Defina
# um nome seguido pela palavra app, por exmeplo "lojaapp"
# ou "projetoapp").

conda create -n nome_do_projeto_que_voce_escolher

# Liste os ambientes criados.

conda env list

# Remover ambiente virtual de programacao.

conda env remove -n nome_do_projeto_que_voce_escolher 

# Ative o ambiente criado. 
# Verifique se no início da linha comandos aparece o nome 
# do projeto entre parenteses conforme o seguinte exemplo
# "(modeloapp) Antonio:~ antonio$".

conda activate nome_do_projeto_que_voce_escolher

# Desative o ambiente. 
# Verifique se no início da linha de comandos desaparece
# o nome entre parenteses conforme o seguinte exemplo 
# "Antonio:~ antonio$".

conda deactivate


#######################################################
# As etapas a seguir devem ser executadas dentro      #
# do ambiente virtual de desenvolvimento do miniconda #
# para cada projeto. Ou seja com o conda atividado    #
# como por exemplo "(modeloapp) Antonio:~ antonio$"	  #
#######################################################

#############################################
# Instalação de bibliotecas Python e Djando #
#############################################

# Utilizar o terminal(Command Prompt) do VSCODE faça todas as 
# operacoes (Para os usuarios de windows nao utilize o PowerShell)

# Instalar o PIP atraves do Miniconda para gerenciamento de pacotes padrao  
# e usado para instalar e gerenciar pacotes de software escritos em Python 
# (A regra para instalação de pacotes, bibliotecas  e dependências, será 
# sempre instalar com o MINICONDA e caso nao tenha utilizar o PIP).

conda install pip

# Instalar Biblioteca "python-decouple" para esconder informações 
# importantes por segurança como as de banco de dados e chave de
# registro do sistema em um arquivo separado chamado exatamente de
# ".env" com essas informações.

pip install python-decouple

# Instalar Biblioteca do driver do banco de dados postgres 
# "psycopg2-binary" para rodar no Framework Django.

pip install psycopg2-binary 

# Instalar biblioteca "Pillow" para tratar e resolver imagens
# para campos do Model Fields (ImageFields).

conda install Pillow

# Instalar Biblioteca "django-widget-tweaks" para renderizar 
# de templates, ajuda a trabalhar com os forms de formas com 
# tags especificas.

pip install django-widget-tweaks

# Instalar o Framework Django.

conda install django


############################################
# Conferência de instalação de Bibliotecas #
############################################

# Digite o comando para listas as bibliotecas instaladas.

pip list

# Digite o comando para listas as bibliotecas instaladas.

conda list


##############################################
# Criacao e configuracao do Framework Django #
##############################################

# Crie um projeto Django em um diretório de sua escolha onde
# ficarao todos os seus projetos (Defina com o mesmo nome do 
# ambiente virtual por exmeplo "lojaapp" ou "projetoapp").

django-admin startproject nome_do_projeto_que_voce_escolher

# O comando criará a seguinte estrutura de pastas.

  (RAIZ)nome_do_projeto_que_voce_escolher
      .   
      ├── manage.py
      └── nome_do_projeto_que_voce_escolher
          ├── __init__.py
          ├── asgi.py
          ├── settings.py
          ├── urls.py
          └── wsgi.py

# Acesse o diretorio RAIZ do projeto criado, e através do 
# terminal inicie o serviço do Django. Lembre que dependendo
# do sitema operacional o "manage.py" pode ser executado de
# forma diferente, por exemplo sem o "./" .

./manage.py runserver

# Depedendo da forma que o python foi instalado ele precisa 
# ser executado com a chamada do Python na frente.

python manage.py runserver

# Acessar um navegador de sua escolha, digitar para testar o 
# servico de servidor web socket criado pelo django.

http://localhost:8000

# Para parar o serviço.

Ctrl + C 

# Caso desejar iniciar o serviço utilizando outra porta como por exemplo 8001.

./manage.py runserver 8001









