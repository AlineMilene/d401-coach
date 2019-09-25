from django.db import models
from django.utils import timezone

class Coach(models.Model):
    nome = models.CharField(max_length=255, verbose_name='Nome')
    frase = models.TextField()
    inspirador = models.CharField(max_length=255, null=True)
    # null = campo não obrigatório
    # blank = campo vazio

    criado_em =  models.DateTimeField(default=timezone.now)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome + ' - ' + self.frase ## mostrar no admin o nome e frase 