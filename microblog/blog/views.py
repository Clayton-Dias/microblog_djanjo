from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Postagem
from .forms import PostagemForm
from django.utils import timezone

# Página inicial mostrando todas as postagens
def index(request):
    postagens = Postagem.objects.filter(data_expiracao__gte=timezone.now(), status='ativo')
    return render(request, 'blog/index.html', {'postagens': postagens})

# Página para criar uma nova postagem
def new_post(request):
    if request.method == 'POST':
        form = PostagemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PostagemForm()
    return render(request, 'blog/new_post.html', {'form': form})

