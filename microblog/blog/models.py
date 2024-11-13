from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MaxLengthValidator
from PIL import Image  # Biblioteca para manipulação de imagens
import io  # Biblioteca para manipulação de fluxos de dados em memória
from django.core.files.uploadedfile import InMemoryUploadedFile  # Para manipular arquivos em memória

class Postagem(models.Model):
    # Define as opções de status da postagem (ativo, inativo, deletado)
    STATUS_CHOICES = [
        ('ativo', 'Ativo'),
        ('inativo', 'Inativo'),
        ('deletado', 'Deletado'),
    ]

    id = models.AutoField(primary_key=True)  # Campo auto incrementado para o ID da postagem
    data = models.DateTimeField(auto_now_add=True)  # Data de criação da postagem (automática)
    
    # Título da postagem com validação de comprimento mínimo de 5 caracteres
    title = models.CharField(
        max_length=127,
        validators=[MinLengthValidator(5, "O título deve ter pelo menos 5 caracteres.")],
        blank=False  # O campo título não pode ficar em branco
    )

    # Campo para a imagem da postagem, com a possibilidade de ser opcional (null=True, blank=True)
    imagem = models.ImageField(upload_to='static/microblog/img/', null=True, blank=True)

    # Conteúdo da postagem com validação de comprimento mínimo (10 caracteres) e máximo (255 caracteres)
    conteudo = models.TextField(
        validators=[
            MinLengthValidator(10, "O conteúdo deve ter pelo menos 10 caracteres."),
            MaxLengthValidator(255, "O conteúdo deve ter no máximo 255 caracteres.")
        ],
        blank=False  # O campo conteúdo não pode ficar em branco
    )

    # Status da postagem (ativo, inativo, deletado), com valor padrão 'ativo'
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default='ativo'
    )

    # Data de expiração da postagem
    data_expiracao = models.DateTimeField()

    class Meta:
        # Ordena as postagens pela data de criação (mais recentes primeiro)
        ordering = ['-data']

    def __str__(self):
        # Retorna os primeiros 50 caracteres do conteúdo como representação da postagem
        return self.conteudo[:50]

    # Definindo limites para o tamanho e dimensões da imagem
    max_image = {
        'size': 50,  # Tamanho máximo da imagem em MB
        'width': 256,  # Largura máxima da imagem (em pixels)
        'height': 256,  # Altura máxima da imagem (em pixels)
    }

    def clean(self):
        """
        Método clean() que valida o modelo antes de salvar.
        Realiza validações extras para o tamanho do conteúdo e tamanho da imagem.
        """
        # Valida o comprimento do conteúdo, garantindo que não ultrapasse 255 caracteres
        if len(self.conteudo) > 255:
            raise ValidationError('O conteúdo não pode exceder 255 caracteres.')

        # Valida o tamanho da imagem, garantindo que ela não exceda o limite configurado em MB
        if self.imagem and self.imagem.size > self.max_image['size'] * 1024 * 1024:
            raise ValidationError(f"A imagem não pode exceder {self.max_image['size']} MB.")

    def save(self, *args, **kwargs):
        """
        Sobrescreve o método save() para realizar o redimensionamento da imagem
        antes de salvar o objeto no banco de dados.
        """
        # Se houver uma imagem, redimensiona-a
        if self.imagem:
            img = Image.open(self.imagem)

            # Verifica se as dimensões da imagem excedem o limite configurado
            if img.height > self.max_image['height'] or img.width > self.max_image['width']:
                # Redimensiona a imagem mantendo a proporção
                output_size = (self.max_image['height'], self.max_image['width'])
                img.thumbnail(output_size)

                # Salva a imagem redimensionada em memória
                img_io = io.BytesIO()  # Cria um buffer em memória
                img.save(img_io, format='PNG')  # Salva a imagem em formato PNG no buffer
                img_io.seek(0)  # Posiciona o ponteiro no início do arquivo em memória

                # Substitui a imagem original pela versão redimensionada
                self.imagem = InMemoryUploadedFile(
                    img_io,  # Arquivo de imagem em memória
                    'ImageField',  # Tipo de campo
                    self.imagem.name,  # Nome original da imagem
                    'image/jpeg',  # Tipo MIME da imagem
                    img_io.getbuffer().nbytes,  # Tamanho da imagem em bytes
                    None  # Não há necessidade de um campo de conteúdo
                )

        # Executa a validação do modelo antes de salvar no banco de dados
        self.full_clean()

        # Salva o modelo no banco de dados
        super().save(*args, **kwargs)
