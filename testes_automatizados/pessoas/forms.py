from django import forms
from .models import Pessoa
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

    def clean_cpf(self):
        """
        Este método é o local padrão do Django para lógica customizada de um campo.
        Fluxo:
        1. Pega o dado bruto enviado pelo usuário.
        2. Usa a função `validar_cpf` para garantir que é um CPF válido.
        3. Se for válido, formata para o padrão '000.000.000-00'.
        4. Retorna o valor formatado para ser salvo no banco.
        """
        # 1. Pega o dado bruto que o usuário digitou no campo 'cpf'
        cpf = self.cleaned_data.get('cpf')

        if cpf:
            # 2. Chama nossa função de validação. 
            # Se o CPF for inválido, ela levantará um ValidationError que o Django
            # exibirá corretamente para o usuário no campo 'cpf'.
            validar_cpf(cpf)

            # 3. Se a validação passou, limpamos o CPF para a formatação.
            cpf_limpo = re.sub(r'[^0-9]', '', cpf)

            # 4. Formata e retorna o valor que será salvo no banco.
            return f"{cpf_limpo[:3]}.{cpf_limpo[3:6]}.{cpf_limpo[6:9]}-{cpf_limpo[9:]}"
        
        # Retorna o valor original caso esteja vazio (se o campo não for obrigatório)
        return cpf