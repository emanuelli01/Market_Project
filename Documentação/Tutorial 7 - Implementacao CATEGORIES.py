####################################
########## APP categories ########## 
####################################

# Acesse a pastas "apps" e crie a estrutura basica de um projeto que 
# sera o nucleo desse projeto "categories". Como sera necessario acessar 
# a pasta "apps" o caminho da pasta manage.py pode alterar 
# dependendo do seu ambiente. 

# No linuxOS e no MacOS o caminho das barras ao contrario ""../manage.py startapp categories" isso 
# tambem serve para as referencias de pastas

..\manage.py startapp categories

# Retorne para a raiz do projeto caso ainda esteja dentro da pasta apps.

cd ..


############
# SETTINGS #
############

# Acesse o arquivo "settings.py" e procure por INSTALLED_APPS e adicione 
# dentro dos colchetes a nova linha a seguir para declarar o categorias 
# do projeto "categories". Nao esqueca das virgulas.

'categories.apps.CategoriesConfig',


########
# APPS #
########

# Acesse o arquivo "apps.py" no caminho "apps/categories/apps.py".
# Procure na classe "CategoriesConfig" o atributo "name = 'categories" e depois 
# desse atributo adicione a linha com o atributo com a identificao ou nome que 
# voce deseja colocar em seu aplicativo.
   
verbose_name = 'Categorias'


########
# URLS #
########

# Na raiz do projeto acesse o arquivo "urls.py" 
# Adicione o caminho da entidade após "path('admin/', admin.site.urls),".

path('categorias/', include('categories.urls', namespace='categories')),

# Criar um "urls.py" dentro dos arquivos de configuracao do categoria em "apps/categories".
# Nesse local serao declaradas as urls especificas do App categories. Adicionar ao arquivo 
# as linhas a seguir.

from django.urls import path
from . import views

app_name = 'categories'

urlpatterns = [
    path('', views.list_categories, name='list_categories'),
    path('adicionar/', views.add_category, name='add_category'),
    path('editar/<int:id_category>/', views.edit_category, name='edit_category'),
    path('excluir/<int:id_category>/', views.delete_category, name='delete_category'),
]


##########
# MODELS #
##########

# Acesse o arquivo "models.py" no caminho "apps/categories/models.py" e 
# construa seus modelos baseado no seu projeto.

# Após o comentario "# Create your models here." e crie a classe "Category" do modelo.

class Category(models.Model):
    name = models.CharField('Nome', max_length=50)
    description = models.TextField('Descricao', max_length=100) 
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering =['id']

    def __str__(self):
        return self.name


#########
# FORMS #
#########

# No caminho "apps/categories/" crie um arquivo "forms.py" e coloque o 
# conteudo para declarar o modelo no forms. Essa etapa é o carregamento 
# do modelo para o forms.

from django import forms
from .models import Category

class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        exclude = ()


#########
# VIEWS #
#########

# Acesse o arquivo "views.py" no caminho "apps/categories/views.py" e 
# construa seus modelos baseado no seu projeto.

# Import os componentes no "django.shortcuts" adicione o "get_object_or_404" e "redirect" 
# para fazer coleta de objetos e redirecionamentos. O import deve ficar da seguinte forma:

from django.shortcuts import render, get_object_or_404, redirect

# Logo a seguir faça os importes dos seguintes componentes.

from .forms import CategoryForm
from .models import Category

# Após o comentario "# Create your views here." e crie as views "Category".

def add_category(request):
    template_name = 'categories/add_category.html'
    context = {}
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('categories:list_categories')
    form = CategoryForm()
    context['form'] = form
    return render(request, template_name, context)

def list_categories(request):
    template_name = 'categories/list_categories.html'
    categories = Category.objects.filter()
    context = {
        'categories': categories
    }
    return render(request, template_name, context)

def edit_category(request, id_category):
    template_name = 'categories/add_category.html'
    context ={}
    category = get_object_or_404(Category, id=id_category)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories:list_categories')
    form = CategoryForm(instance=category)
    context['form'] = form
    return render(request, template_name, context)

def delete_category(request, id_category):
    category = Category.objects.get(id=id_category)
    category.delete()
    return redirect('categories:list_categories')


#############
# TEMPLATES #
#############

# Crie uma pasta dentro de "templates" com o nome do "categories".

# Criar um arquivo "add_category.html" com as informacoes de formulario 
# para adicionar categorias.

{% extends 'base.html' %}
{% load widget_tweaks %} 

{% block title %}

    Adicionar Categoria - {{ block.super }}

{% endblock title %}

{% block body %}

    <div class="container">
        <br />
    <h5><b>Cadastro de Categoria</b></h5>
        <div class="row">
            <div class ="col-md-12">
                <form action="" method="POST">
                {% csrf_token %}
                <div class="form-group">
                   <label for="{{ form.name.id_for_label }}">Nome</label>
                   {{ form.name|add_class:"form-control" }}
                </div>
                <div class="form-group">
                    <label for="{{ form.description.id_for_label }}">Descricao</label>
                    {{ form.description|add_class:"form-control" }}
                 </div>
                    <button type="submit" class="btn btn-primary">Salvar</button>       
                </form>
            </div>
        </div>
    </div>

{% endblock body %}

# Criar um arquivo "list_categories.html" com as informacoes em lista dos categorias adicionados.

{% extends 'base.html' %}

{% block title %}

    Lista de Categorias - {{ block.super }}

{% endblock title %}

{% block body %}

    <div class="container">
        <br />
        <h5><b>Lista de Categorias</b></h5>
        <div class="row">
            <div class ="col-md-12">
                <br />
                    <a href="{% url 'categories:add_category' %}">Cadastro de nova categoria</a>
                <br />
                <br />
                <table class="table table-hover">
                <thead>
                    <tr>
                    <th scope="col">#</th>
                    <th scope="col">Nome</th>
                    <th scope="col">Descricao</th>
                    <th scope="col"></th>
                    <th scope="col"></th>
                    </tr>
                </thead>
                <tbody>
                    {% for category in categories %}
                        <tr>
                            <th scope="row">{{ category.id }}</th>
                            <td>{{ category.name }}</td>
                            <td>{{ category.description }}</td>
                            <td>
                                <a href="{% url 'categories:edit_category' category.id %}" class="btn btn-primary btn-sm">Editar</a>
                            </td>
                            <td>
                                <a href="{% url 'categories:delete_category' category.id %}" class="btn btn-danger btn-sm ">Excluir</a>
                            </td>
                        </tr> 
                    {% endfor %}
                </tbody>
                </table>
            </div>
        </div>
    </div>

{% endblock body %}

# Acesse o arquivo "base.html" para inserir os links no menu. Siga até o 
# menu dropdown no link "Categoria" e insira os urls.

{% url 'categories:list_categories' %}

# Criar uma migracao do projeto a partir do modelo criado categorias.

./manage.py makemigrations

# Para o caso dos campos models fields sera necessario setar o "timezone.now" para 
# pegar a data hora atual do sistema, logo sera necessario confirmar essa questao.
# Aparecera a seguinte mensagem e voce devera clicar na tebla ENTER para confirmar.

# Apos a mensagem clique "ENTER".

#  Please enter the default value now, as valid Python
#  You can accept the default 'timezone.now' by pressing 'Enter' or you can provide another value.
#  The datetime and django.utils.timezone modules are available, so you can do e.g. timezone.now
#  Type 'exit' to exit this prompt
#  [default: timezone.now] >>> 

# Clique na tecla ENTER

# Executar efetivamente as migracoes criadas.

./manage.py migrate

# Inicie o servico http e teste a aplicacao no navegador.

./manage.py runserver








