# MARKET E-COMMERCE

Sistema feito como projeto final de semestre, tive como objetivo principal, criar um sistema híbrido centrado na facilidade do usuário sem conhecimento técnico, ter a praticidade em fazer suas compras online de forma objetiva, tanto por via web, quanto por dispositivos móveis, tudo a partir do conforto de sua casa.
Neste projeto, o administrador tem o direito de adicionar novas categorias e produtos, ao passo que o usuário tem a capacidade de navegar pela lista de produtos conforme suas categorias e adicioná-los ao carrinho.

## Tecnologias utilizadas

<div align="left">
	<code><img width="50" src="https://www.vectorlogo.zone/logos/postgresql/postgresql-icon.svg" alt="HTML" title="HTML"/></code>
	<code><img width="50" src="https://logospng.org/wp-content/uploads/javascript.png" alt="HTML" title="HTML"/></code>
	<code><img width="50" src="https://www.vectorlogo.zone/logos/getbootstrap/getbootstrap-icon.svg" alt="HTML" title="HTML"/></code>
	<code><img width="50" src="https://www.vectorlogo.zone/logos/python/python-icon.svg" alt="HTML" title="HTML"/></code>
	<code><img width="50" src="https://www.vectorlogo.zone/logos/djangoproject/djangoproject-ar21.svg" alt="HTML" title="HTML"/></code>
	<code><img width="50" src="https://user-images.githubusercontent.com/25181517/192158954-f88b5814-d510-4564-b285-dff7d6400dad.png" alt="HTML" title="HTML"/></code>
	<code><img width="50" src="https://user-images.githubusercontent.com/25181517/183898674-75a4a1b1-f960-4ea9-abcb-637170a00a75.png" alt="CSS" title="CSS"/></code>
	<code><img width="50" src="https://avatars.githubusercontent.com/u/6392739?s=280&v=4" alt="CSS" title="CSS"/></code>
</div>

## Como elas foram usadas
### O modelo de desenvolvimento foi influenciado pelo framework Django, criado para facilitar o desenvolvimento rápido na web. Em termos gerais, o fluxo de requisição no Django segue a seguinte lógica: quando uma requisição é recebida pelo servidor, ela passa pelos endpoints. Após localizar o endpoint adequado, o sistema resolve a URL e direciona a requisição para uma visão (view). Essa visão pode interagir com o banco de dados por meio dos modelos (models) e, finalmente, retorna um template. Resumidamente, o Django simplifica o processo de desenvolvimento web, desde a gestão de requisições até a apresentação visual por meio de templates.



# Para execução
- Ter o ambiente virtual com todas as dependências listadas abaixo. (Mini Conda)
- Executar o arquivo manage.py na raiz do projeto por linha de comando "manage.py runserver".

## Dependências
### Conda
- pip
- django

### Pip
- python-decouple
- psycopg2-binary
- djangorestframework
- markdown
- django-filter
