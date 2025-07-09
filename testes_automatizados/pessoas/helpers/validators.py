import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validar_cpf(value):
    cpf_limpo = re.sub(r'[^0-9]', '', str(value))

    if len(cpf_limpo) != 11 or cpf_limpo == cpf_limpo[0] * 11:
        raise ValidationError(_('CPF inválido.'), code='invalid')

    def calcular_digito(digitos):
        soma = sum(int(d) * i for d, i in zip(digitos, range(len(digitos) + 1, 1, -1)))
        resto = (soma * 10) % 11
        return str(resto if resto < 10 else 0)

    digito1 = calcular_digito(cpf_limpo[:9])
    digito2 = calcular_digito(cpf_limpo[:9] + digito1)

    if cpf_limpo[-2:] != digito1 + digito2:
        raise ValidationError(_('CPF inválido.'), code='invalid')