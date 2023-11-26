from django.urls import path
from inicio.views import index, imagem, lista_produtos, adicionar_produto


urlpatterns = [
    path("", index, name="index"),
    path("imagem/", imagem, name="imagem"),
    path("lista/", lista_produtos, name="lista_produtos"),
    path("adicionar/", adicionar_produto, name="adicionar_produto"),
]
