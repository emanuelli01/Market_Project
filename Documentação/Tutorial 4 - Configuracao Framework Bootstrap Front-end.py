#################################
# Framework Bootstrap Front-end #
#################################

# Baixe ou crie os arquivos de JavaScript de seu front-end na pasta "staticfiles/js".

bootstrap.min.js
jquery-ui.js
jquery-3.5.1.min.js
jquery.mask.min.js

# Baixe ou crie os arquivos de estilos de seu front-end na pasta "staticfiles/css".

bootstrap.min.css
jquery-ui.css
signin.css


# Na raiz da pasta "templates" crie um aquivo "base.html" com a estrutura
# basica de html 5. Essa pasta ira conter as tags comuns para todos os 
# arquivos htmls da maioria dos "apps" do projeto. Digite o codigo a seguir.

{% load static %}

<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="{% static 'css/jquery-ui.css' %}">
    <link rel="stylesheet" href="{% static 'css/bootstrap.min.css' %}">
    <title>{% block title %}Nome do meu App{% endblock title %}</title>
</head>
<body>

    {% block body %}
    
    {% endblock body %}
    
    <script src="{% static 'js/jquery-3.5.1.min.js' %}"></script>
    <script src="{% static 'js/jquery.mask.min.js' %}"></script>
    <script src="{% static 'js/jquery-ui.js' %}"></script>
    <script src="{% static 'js/bootstrap.min.js' %}"></script>
</body>
</html>

# Importar biblioteca para aplicar bootstrap em campos de form

'widget_tweaks',
