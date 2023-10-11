import os
from uuid import uuid4
from django.db import models
from django.contrib.auth.models import AbstractUser

def safe_rename(instance, filename): # função para renomear o arquivo de forma segura
    extension = filename.split('.')[-1]
    filename = f'{uuid4().hex}.{extension}'
    return os.path.join('images', filename)


# Create your models here.
class CustomUser(AbstractUser):
    data_nascimento = models.DateField(
            "Data nascimento",
            null=True,
            blank=True
        )
    cpf = models.CharField("CPF", max_length=11, null=True, blank=True)
    imagem = models.FileField(
        upload_to=safe_rename,
        default=None,
        null=True,
        blank=True
    )


