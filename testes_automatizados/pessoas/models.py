from django.core.exceptions import ValidationError
from django.db import models
from datetime import date

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True, verbose_name="CPF")
    data_nascimento = models.DateField()
    email = models.EmailField()

    def clean(self):
        if self.data_nascimento and self.data_nascimento > date.today():
            raise ValidationError({'data_nascimento': 'A data de nascimento não pode ser futura.'})

    def __str__(self):
        return f"{self.nome} - {self.cpf}"