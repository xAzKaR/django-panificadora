from django.shortcuts import redirect, render
from inicio.forms import ProdutoForm
from inicio.models import Produto


def index(request):
    return render(request, "pages/index.html")


def imagem(request):
    return render(request, "pages/imagem.html")


def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, "pages/lista-produtos.html", {"produtos": produtos})


def adicionar_produto(request):
    if request.method == "POST":
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_produtos")  # Redireciona para lista de produtos
    else:
        form = ProdutoForm()

    return render(request, "pages/adicionar_produto.html", {"form": form})
