from django.urls import path
from .views import list_hortifruti_products

app_name = 'hortifruti'

urlpatterns = [
    path('', list_hortifruti_products, name='list_hortifruti_products'),
]
