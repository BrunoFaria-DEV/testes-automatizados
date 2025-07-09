from django import forms
from .models import Pessoa
from datetime import date
from .helpers.validators import validar_cpf
import re

class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = ['nome', 'cpf', 'data_nascimento', 'email']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'input-text'}),
            'cpf': forms.TextInput(attrs={'class': 'input-text'}),
            'email': forms.EmailInput(attrs={'class': 'input-text'}),
        }

    data_nascimento = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'input-data'}),
        input_formats=['%Y-%m-%d'],
        label='Data de Nascimento'
    )

    def clean_data_nascimento(self):
        data = self.cleaned_data.get('data_nascimento')
        if data and data > date.today():
            raise forms.ValidationError('A data de nascimento não pode ser futura.')
        return data

    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf')

        if cpf:
            validar_cpf(cpf)
            cpf_limpo = re.sub(r'[^0-9]', '', cpf)
            cpf_formatado = f"{cpf_limpo[:3]}.{cpf_limpo[3:6]}.{cpf_limpo[6:9]}-{cpf_limpo[9:]}"

            if Pessoa.objects.filter(cpf=cpf_formatado).exclude(pk=self.instance.pk).exists():
                raise forms.ValidationError('Este CPF já está cadastrado.')

            return cpf_formatado

        return cpf