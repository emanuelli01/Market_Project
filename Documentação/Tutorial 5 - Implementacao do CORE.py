##############################
########## APP core ##########
##############################

# Acesse a pastas "apps" e crie a estrutura basica de um projeto que
# sera o nucleo desse projeto "core". Como sera necessario acessar a
# pasta "apps" o caminho da pasta manage.py pode mudar dependendo 
# do seu ambiente. 

# No linuxOS e no MacOS o caminho das barras ao contrario ""../manage.py startapp core" 
# isso tambem serve para as referencias de pastas

# Acessar pasta

cd apps

# rodar a criacao de Apps

..\manage.py startapp core

# Retorne para a raiz do projeto caso ainda esteja dentro da pasta apps.

cd ..


############
# SETTINGS #
############

# Retorne para a raiz do projeto caso ainda esteja dentro da pasta apps.

# Acesse o arquivo "settings.py" e procure por INSTALLED_APPS e adicione dentro 
# dos colchetes a nova linha a seguir para declarar o nucleo do projeto "core". 
# Nao esqueca das virgulas.

'core.apps.CoreConfig', 


########
# APPS #
########

# Acesse o arquivo apps.py no caminho "apps/core/apps.py"

# Aprocure na classe "CoreConfig" o atributo "name = 'core'" e depois desse atributo 
# adicione a linha com o atributo com a identificao ou nome que voce deseja colocar 
# em seu aplicativo.
   
verbose_name = 'Nome do seu App'


########
# URLS #
########

# Na raiz do projeto acesse o arquivo "urls.py". Nesse local serao declaradas as urls
# geral de cada App. 

# Adicione o caminho da entidade apos o " path('admin/', admin.site.urls),".

path('', include('core.urls', namespace='core')),

# Criar um arquivo "urls.py" dentro dos arquivos de configuracao do core em "apps/core".
# Nesse local serao declaradas as urls especificas do App Core.

# Adicionar ao arquivo.

from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
]


#########
# VIEWS #
#########

# Acesse a pasta "apps/core/view.py"

# Criar metodo/funcao para redenrizar a pagina apos o "# Create your views here.". 

def home(request):
    template_name ='core/home.html'
    context = {}
    return render(request, template_name, context)




