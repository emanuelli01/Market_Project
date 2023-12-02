###################################
########## APP products ########## 
###################################

# Acesse a pastas "apps" e crie a estrutura basica de um projeto que 
# sera o nucleo desse projeto "products". Como sera necessario acessar 
# a pasta "apps" o caminho da pasta manage.py pode alterar dependendo 
# do seu ambiente. 

# No linuxOS e no MacOS o caminho das barras ao contrario ""../manage.py startapp products" isso 
# tambem serve para as referencias de pastas

..\manage.py startapp products

# Retorne para a raiz do projeto caso ainda esteja dentro da pasta apps.

cd ..


############
# SETTINGS #
############

# Acesse o arquivo "settings.py" e procure por INSTALLED_APPS e adicione 
# dentro dos colchetes a nova linha a seguir para declarar o produtos do 
# projeto "products". Nao esqueca das virgulas.

'products.apps.ProductsConfig',


########
# APPS #
########

# Acesse o arquivo "apps.py" no caminho "apps/products/apps.py".
# Procure na classe "ProductsConfig" o atributo "name = 'products" e depois 
# desse atributo adicione a linha com o atributo com a identificao ou nome 
# que voce deseja colocar em seu aplicativo.
   
verbose_name = 'Produtos'


########
# URLS #
########

# Na raiz do projeto acesse o arquivo "urls.py" 
# Adicione o caminho da entidade após "path('admin/', admin.site.urls),".

path('produtos/', include('products.urls', namespace='products')),

# Criar um "urls.py" dentro dos arquivos de configuracao do cproduto em "apps/products".
# Nesse local serao declaradas as urls especificas do App products. Adicionar ao arquivo 
# as linhas a seguir.

from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.list_products, name='list_products'),
    path('adicionar/', views.add_product, name='add_product'),
    path('editar/<int:id_product>/', views.edit_product, name='edit_product'),
    path('excluir/<int:id_product>/', views.delete_product, name='delete_product'),
]


##########
# MODELS #
##########

# Acesse o arquivo "models.py" no caminho "apps/products/models.py" e construa 
# seus modelos baseado no seu projeto.

# Importe o modelo de "Category" para adicionar o relacionamento da chave estrangeira 
# indicando a propriedade do modelo ao categorias criado.

from categories.models import Category

# Após o comentario "# Create your models here." e crie a classe "Product" do modelo.

class Product(models.Model):
    name = models.CharField('Nome', max_length=50)
    date_fabrication = models.DateField('Data Fabricacao', auto_now=False, auto_now_add=False) 
    is_active = models.BooleanField('Ativo', default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering =['id']

    def __str__(self):
        return self.name


#########
# FORMS #
#########

# No caminho "apps/products/" crie um arquivo "forms.py" e coloque o conteudo 
# para declarar o modelo no forms e exclua da visualizacao o campo user para 
# que nao fique visivel. Essa etapa é o carregamento do modelo para o forms.

from django import forms
from .models import Product

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        exclude = ()


#########
# VIEWS #
#########

# Acesse o arquivo "views.py" no caminho "apps/products/views.py" e 
# construa seus modelos baseado no seu projeto.

# Import os componentes no "django.shortcuts" adicione o "get_object_or_404" e "redirect" 
# para fazer coleta de objetos e redirecionamentos. O import deve ficar da seguinte forma:

from django.shortcuts import render, get_object_or_404, redirect

# Logo a seguir faça os importes dos seguintes componentes.

from .forms import ProductForm
from .models import Product

# Após o comentario "# Create your views here." e crie as views "Product".

def add_product(request):
    template_name = 'products/add_product.html'
    context = {}
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('products:list_products')
    form = ProductForm()
    context['form'] = form
    return render(request, template_name, context)

def list_products(request):
    template_name = 'products/list_products.html'
    products = Product.objects.filter()
    context = {
        'products': products
    }
    return render(request, template_name, context)

def edit_product(request, id_product):
    template_name = 'products/add_product.html'
    context ={}
    product = get_object_or_404(Product, id=id_product)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES,  instance=product)
        if form.is_valid():
            form.save()
            return redirect('products:list_products')
    form = ProductForm(instance=product)
    context['form'] = form
    return render(request, template_name, context)

def delete_product(request, id_product):
    product = Product.objects.get(id=id_product)
    product.delete()
    return redirect('products:list_products')


#############
# TEMPLATES #
#############

# Crie uma pasta dentro de "templates" com o nome do "products".

# Criar um arquivo "add_product.html" com as informacoes de formulario 
# para adicionar produtos. 
# Nesse form foi adicionado o parametro " enctype="multipart/form-data" " 
# que permite que arquivos sejam enviados por meio de um POST.Se você 
# deseja permitir que um usuário faça upload de um arquivo por meio de
# um formulário deve adicionar esse parametro.

{% extends 'base.html' %}

{% load widget_tweaks %}

{% block title %}

    Adicionar Produto - {{ block.super }}

{% endblock title %}

{% block body %}

    <div class="container">
        <br />
    <h5><b>Cadastro de Produto</b></h5>
        <div class="row">
            <div class ="col-md-12">
                <form action="" method="POST" enctype="multipart/form-data"> 
                {% csrf_token %}
                <div class="form-group">
                   <label for="{{ form.name.id_for_label }}">Nome</label>
                   {{ form.name|add_class:"form-control" }}
                </div>
                <div class="form-group">
                    <label for="{{ form.date_fabrication.id_for_label }}">Data de fabricacao</label>
                    {{ form.date_fabrication|add_class:"form-control" }}
                </div>
                <div class="form-group">
                    <label for="{{ form.is_active.id_for_label }}">Ativar</label>
                    {{ form.is_active }}
                </div>
                <div class="form-group">
                    <label for="{{ form.category.id_for_label }}">Categoria</label>
                    {{ form.category|add_class:"form-control" }}
                </div>
                    <button type="submit" class="btn btn-primary">Salvar</button>       
                </form>
            </div>
        </div>
    </div>

{% endblock body %}

# Criar um arquivo "list_products.html" com as informacoes em lista dos produtos adicionados.

{% extends 'base.html' %}

{% block title %}

    Lista de Produtos - {{ block.super }}

{% endblock title %}

{% block body %}

    <div class="container">
        <br />
        <h5><b>Lista de Produtos</b></h5>
        <br />
            <a href="{% url 'products:add_product' %}">Cadastro de novo produto</a>
        <br />
        <br />
        <div class="row">
            <div class ="col-md-12">
                <table class="table table-hover">
                <thead>
                    <tr>
                    <th scope="col">#</th>
                    <th scope="col">Nome</th>
                    <th scope="col">Data de fabricacao</th>
                    <th scope="col">Ativo</th>
                    <th scope="col">Categoria</th>
                    <th scope="col"></th>
                    <th scope="col"></th>
                    </tr>
                </thead>
                <tbody>
                    {% for product in products %}
                        <tr>
                            <th scope="row">{{ product.id }}</th>
                            <td>{{ product.name }}</td>
                            <td>{{ product.date_fabrication }}</td>
                            <td>
                                {% if product.is_active == True %}
                                    Ativo
                                {% endif %}
                                {% if product.is_active == False %}
                                    Inativo
                                {% endif %}
                            </td>
                            <td>{{ product.category }}</td>
                            <td>
                                <a href="{% url 'products:edit_product' product.id %}" class="btn btn-primary btn-sm">Editar</a>
                            </td>
                            <td>    
                                <a href="{% url 'products:delete_product' product.id %}" class="btn btn-danger btn-sm ">Excluir</a>
                            </td>
                        </tr> 
                    {% endfor %}
                </tbody>
                </table>
            </div>
        </div>
    </div>

{% endblock body %}

# Acesse o arquivo "base.html" para inserir os links no menu. Siga até o menu dropdown 
# no link "Produto" e insira os urls.

{% url 'products:list_products' %}

# Criar uma migracao do projeto a partir do modelo criado produtos.

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





