from django import forms  # Importa o módulo de formulários do Django
from .models import Postagem  # Importa o modelo 'Postagem' da aplicação local

class PostagemForm(forms.ModelForm):  # Define a classe do formulário, que herda de ModelForm
    class Meta:  # A classe Meta contém configurações adicionais para o formulário
        model = Postagem  # Especifica que o formulário é baseado no modelo 'Postagem'
        
        fields = ['title', 'conteudo', 'imagem', 'data_expiracao']  # Define os campos do modelo que aparecerão no formulário
        
        widgets = {  # Personaliza a forma como alguns campos serão exibidos no formulário
            'data_expiracao': forms.DateTimeInput(attrs={'type': 'datetime-local'}),  # O campo 'data_expiracao' usará um seletor de data e hora no formato local
        }

        labels = {  # Personaliza os rótulos que serão exibidos para o usuário ao lado dos campos
            'title': 'Título',  # Rótulo personalizado para o campo 'title'
            'imagem': 'Imagem',  # Rótulo personalizado para o campo 'imagem'
            'data_expiracao': 'Data de expiração',  # Rótulo personalizado para o campo 'data_expiracao'
        }
