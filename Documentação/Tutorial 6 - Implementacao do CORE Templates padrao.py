#########################
# TEMPLATES PADRAO CORE #
#########################

# Acesse site o bootstrap e baixe um modelo de layout com menu ou 
# utilize o definino em aula.

# Acesse pasta "templates".

# Crie um arquivo arquivo "base.html" cole o codigo bootstrap do navbar
# e menu drodowh após o "<body>".

<!-- INICIO: Bloco do Bootstrap a ser incluido -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <a class="navbar-brand" href="/">Nome do meu App</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarsExample05" aria-controls="navbarsExample05" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarsExample05">
            <ul class="navbar-nav mr-auto">
                <li class="nav-item dropdown">
                    <a class="nav-link dropdown-toggle" href="#" id="dropdown05" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">Menu</a>
                    <div class="dropdown-menu" aria-labelledby="dropdown05">
                        <a class="dropdown-item" href="#">Produtos</a>
                        <a class="dropdown-item" href="#">Categorias</a>
                    </div>
                </li>
            </ul>
        </div>
    </nav>
    <!-- FIM: Bloco do Bootstrap a ser incluido -->

# Crie uma pasta "core" para htmls que irao compor a entidade CORE.

# Criar um arquivo "home.html" somente com o html especifico desse 
# arquivo o resto puxa automaticamente do "base.html".

{% extends 'base.html' %}

{% block title %}
    {{ block.super }}
{% endblock title %}

{% block body %}

<!-- Codigo html especifico desse arquivo -->

{% endblock body %}

# Inicie o servico http e teste a aplicacao no navegador.

./manage.py runserver





