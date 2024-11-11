from django.db import models

# Create your models here.

class Postagem(models.Model):
    STATUS_CHOICES = [
        ('ativo', 'Ativo'),
        ('inativo', 'Inativo'),
    ]

    id = models.AutoField(primary_key=True)
    data = models.DateTimeField(auto_now_add=True)
    imagem = models.ImageField(upload_to='postagens/', blank=True, null=True)
    conteudo = models.CharField(max_length=255)
    status = models.CharField(max_length=7, choices=STATUS_CHOICES, default='ativo')
    data_expiracao = models.DateTimeField()

    def __str__(self):
        return self.conteudo[:50]  # Exibe os primeiros 50 caracteres do conteúdo

    class Meta:
        ordering = ['-data']  # Ordena as postagens pela data mais recente