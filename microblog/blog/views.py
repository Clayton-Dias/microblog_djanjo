from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Postagem
from .forms import PostagemForm
from django.utils import timezone
from django.contrib import messages

# Página inicial mostrando todas as postagens ativas
def index(request):
    # Filtra as postagens ativas e que não expiraram ainda (data_expiracao maior ou igual ao tempo atual)
    postagens = Postagem.objects.filter(data_expiracao__gte=timezone.now(), status='ativo')
    # Renderiza a página inicial passando a lista de postagens como contexto
    return render(request, 'blog/index.html', {'postagens': postagens})

# Página para criar uma nova postagem
def new_post(request):
    if request.method == 'POST':  # Se o método de requisição for POST (quando o formulário for enviado)
        form = PostagemForm(request.POST, request.FILES)  # Cria o formulário com os dados do POST e arquivos enviados
        if form.is_valid():  # Verifica se o formulário é válido (com as validações do formulário no modelo)
            form.save()  # Salva a nova postagem no banco de dados
            messages.success(request, 'Postagem criada com sucesso!')
            return redirect('index')  # Redireciona para a página de sucesso (definida em success)
    else:
        form = PostagemForm()  # Se não for um POST, apenas cria um formulário vazio
    return render(request, 'blog/new_post.html', {'form': form})  # Renderiza a página de criação de postagem com o formulário

# Página sobre
def about(request):
    return render(request, 'blog/about.html')  # Renderiza a página 'about'

# Página de sucesso após salvar a postagem
def success(request):
    return render(request, 'blog/success.html')  # Renderiza a página de sucesso (por exemplo, uma confirmação)

