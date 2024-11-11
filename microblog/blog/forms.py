from django import forms
from .models import Postagem

class PostagemForm(forms.ModelForm):
    class Meta:
        model = Postagem
        fields = ['conteudo', 'imagem', 'data_expiracao', 'status']
        widgets = {
            'data_expiracao': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }