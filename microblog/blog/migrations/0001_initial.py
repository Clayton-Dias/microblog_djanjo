# Generated by Django 5.1.3 on 2024-11-11 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Postagem',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='postagens/')),
                ('conteudo', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('ativo', 'Ativo'), ('inativo', 'Inativo')], default='ativo', max_length=7)),
                ('data_expiracao', models.DateTimeField()),
            ],
            options={
                'ordering': ['-data'],
            },
        ),
    ]
