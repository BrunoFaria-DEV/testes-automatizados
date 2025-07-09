from django.test import TestCase
from django.urls import reverse
from pessoas.models import Pessoa

class ListarPessoasSemCadastrosView(TestCase):
    def test_lista_pessoas_view_acessada_com_sucesso(self):
        response = self.client.get(reverse('lista_pessoas'))
        self.assertEqual(response.status_code, 200)

    def test_lista_pessoas_view_renderiza_template_esperado(self):
        response = self.client.get(reverse('lista_pessoas'))
        self.assertTemplateUsed(response, 'pessoas/lista.html')

    def test_lista_pessoas_view_renderiza_template_com_elemento_log(self):
        response = self.client.get(reverse('lista_pessoas'))
        self.assertContains(response, 'VIEW: lista_pessoas')

    def test_lista_pessoas_view_renderiza_botao_novo(self):
        response = self.client.get(reverse('lista_pessoas'))
        self.assertContains(response, 'href="/pessoas/criar/"')
        self.assertContains(response, '>Novo</a>')

class TesteCriarPessoaView(TestCase):
    def test_criar_pessoa_view_acessada_com_sucesso(self):
        response = self.client.get(reverse('criar_pessoa'))
        self.assertEqual(response.status_code, 200)

    def test_criar_pessoa_view_renderiza_template_esperado(self):
        response = self.client.get(reverse('criar_pessoa'))
        self.assertTemplateUsed(response, 'pessoas/form.html')

    def test_criar_pessoa_view_renderiza_elemento_log(self):
        response = self.client.get(reverse('criar_pessoa'))
        self.assertContains(response, 'VIEW: criar_pessoa')

    def test_criar_pessoa_view_renderiza_formulario(self):
        response = self.client.get(reverse('criar_pessoa'))
        self.assertContains(response, '<form')
        self.assertContains(response, '</form>')  

    def test_criar_pessoa_view_exibe_campos_do_formulario(self):
        response = self.client.get(reverse('criar_pessoa'))
        self.assertContains(response, 'name="nome"')
        self.assertContains(response, 'name="cpf"')
        self.assertContains(response, 'name="data_nascimento"')
        self.assertContains(response, 'name="email"')
    
    def test_criar_pessoa_view_renderiza_botao_submit(self):
        response = self.client.get(reverse('criar_pessoa'))
        self.assertContains(response, 'type="submit"')
        self.assertContains(response, '>Salvar</button>')

class TesteEditarPessoaView(TestCase):
    def test_editar_pessoa_view_acessada_com_sucesso(self):
        dados = {
            'nome': 'João da Silva',
            'cpf': '52998224725',  
            'data_nascimento': '1990-05-10',
            'email': 'joao@email.com'
        }
        Pessoa.objects.create(**dados)
        response = self.client.get(reverse('editar_pessoa', args=[1]))
        self.assertEqual(response.status_code, 200)

    def test_editar_pessoa_view_renderiza_template_esperado(self):
        dados = {
            'nome': 'João da Silva',
            'cpf': '52998224725',  
            'data_nascimento': '1990-05-10',
            'email': 'joao@email.com'
        }
        Pessoa.objects.create(**dados)
        response = self.client.get(reverse('editar_pessoa', args=[1]))
        self.assertTemplateUsed(response, 'pessoas/form.html')

    def test_editar_pessoa_view_renderiza_elemento_log(self):
        dados = {
            'nome': 'João da Silva',
            'cpf': '52998224725',  
            'data_nascimento': '1990-05-10',
            'email': 'joao@email.com'
        }
        Pessoa.objects.create(**dados)
        response = self.client.get(reverse('editar_pessoa', args=[1]))
        self.assertContains(response, 'VIEW: editar_pessoa')

    def test_editar_pessoa_view_renderiza_formulario(self):
        dados = {
            'nome': 'João da Silva',
            'cpf': '52998224725',  
            'data_nascimento': '1990-05-10',
            'email': 'joao@email.com'
        }
        Pessoa.objects.create(**dados)
        response = self.client.get(reverse('editar_pessoa', args=[1]))
        self.assertContains(response, '<form')
        self.assertContains(response, '</form>')  

    def test_editar_pessoa_view_exibe_campos_do_formulario(self):
        dados = {
            'nome': 'João da Silva',
            'cpf': '52998224725',  
            'data_nascimento': '1990-05-10',
            'email': 'joao@email.com'
        }
        Pessoa.objects.create(**dados)
        response = self.client.get(reverse('editar_pessoa', args=[1]))
        self.assertContains(response, 'name="nome"')
        self.assertContains(response, 'name="cpf"')
        self.assertContains(response, 'name="data_nascimento"')
        self.assertContains(response, 'name="email"')

    def test_editar_pessoa_view_renderiza_botao_submit(self):
        dados = {
            'nome': 'João da Silva',
            'cpf': '52998224725',  
            'data_nascimento': '1990-05-10',
            'email': 'joao@email.com'
        }
        Pessoa.objects.create(**dados)
        response = self.client.get(reverse('editar_pessoa', args=[1]))
        self.assertContains(response, 'type="submit"')
        self.assertContains(response, '>Salvar</button>')

class TesteExcluirPessoaView(TestCase):
    def test_excluir_pessoa_view_acessada_com_sucesso(self):
        dados = {
            'nome': 'João da Silva',
            'cpf': '52998224725',  
            'data_nascimento': '1990-05-10',
            'email': 'joao@email.com'
        }
        Pessoa.objects.create(**dados)
        response = self.client.get(reverse('excluir_pessoa', args=[1]))
        self.assertEqual(response.status_code, 200)

    def test_excluir_pessoa_view_renderiza_template_esperado(self):
        dados = {
            'nome': 'João da Silva',
            'cpf': '52998224725',  
            'data_nascimento': '1990-05-10',
            'email': 'joao@email.com'
        }
        Pessoa.objects.create(**dados)
        response = self.client.get(reverse('excluir_pessoa', args=[1]))
        self.assertTemplateUsed(response, 'pessoas/confirmar_exclusao.html')

    def test_excluir_pessoa_view_renderiza_elemento_log(self):
        dados = {
            'nome': 'João da Silva',
            'cpf': '52998224725',  
            'data_nascimento': '1990-05-10',
            'email': 'joao@email.com'
        }
        Pessoa.objects.create(**dados)
        response = self.client.get(reverse('excluir_pessoa', args=[1]))
        self.assertContains(response, 'VIEW: excluir_pessoa')

    def test_excluir_pessoa_view_renderiza_botao_confirmar(self):
        dados = {
            'nome': 'João da Silva',
            'cpf': '52998224725',  
            'data_nascimento': '1990-05-10',
            'email': 'joao@email.com'
        }
        Pessoa.objects.create(**dados)
        response = self.client.get(reverse('excluir_pessoa', args=[1]))
        self.assertContains(response, '<form')
        self.assertContains(response, 'type="submit"')
        self.assertContains(response, '>Confirmar</button>')

class ViewsListarPessoasComCadastrosView(TestCase):
    def test_lista_pessoas_view_acessada_com_sucesso(self):
        dados = {
            'nome': 'João da Silva',
            'cpf': '52998224725',  
            'data_nascimento': '1990-05-10',
            'email': 'joao@email.com'
        }
        Pessoa.objects.create(**dados)
        response = self.client.get(reverse('lista_pessoas'))
        self.assertEqual(response.status_code, 200)

    def test_lista_pessoas_view_renderiza_template_esperado(self):
        dados = {
            'nome': 'João da Silva',
            'cpf': '52998224725',  
            'data_nascimento': '1990-05-10',
            'email': 'joao@email.com'
        }
        Pessoa.objects.create(**dados)
        response = self.client.get(reverse('lista_pessoas'))
        self.assertTemplateUsed(response, 'pessoas/lista.html')

    def test_lista_pessoas_view_renderiza_template_com_elemento_log(self):
        dados = {
            'nome': 'João da Silva',
            'cpf': '52998224725',  
            'data_nascimento': '1990-05-10',
            'email': 'joao@email.com'
        }
        Pessoa.objects.create(**dados)
        response = self.client.get(reverse('lista_pessoas'))
        self.assertContains(response, 'VIEW: lista_pessoas')

    def test_lista_pessoas_view_renderiza_botao_novo(self):
        dados = {
            'nome': 'João da Silva',
            'cpf': '52998224725',  
            'data_nascimento': '1990-05-10',
            'email': 'joao@email.com'
        }
        Pessoa.objects.create(**dados)
        response = self.client.get(reverse('lista_pessoas'))
        self.assertContains(response, 'href="/pessoas/criar/"')
        self.assertContains(response, '>Novo</a>')

    def test_lista_pessoas_view_renderiza_botao_editar(self):
        dados = {
            'nome': 'João da Silva',
            'cpf': '52998224725',  
            'data_nascimento': '1990-05-10',
            'email': 'joao@email.com'
        }
        pessoa = Pessoa.objects.create(**dados)
        response = self.client.get(reverse('lista_pessoas'))
        url_esperada = f'href="/pessoas/editar/{pessoa.id}/"'
        self.assertContains(response, url_esperada)
        self.assertContains(response, '>Editar</a>')

    def test_lista_pessoas_view_renderiza_botao_excluir(self):
        dados = {
            'nome': 'João da Silva',
            'cpf': '52998224725',  
            'data_nascimento': '1990-05-10',
            'email': 'joao@email.com'
        }
        pessoa = Pessoa.objects.create(**dados)
        response = self.client.get(reverse('lista_pessoas'))
        url_esperada = f'href="/pessoas/excluir/{pessoa.id}/"'
        print("\n>>> id da pessoa cadastrada <<<", pessoa.id)
        self.assertContains(response, url_esperada)
        self.assertContains(response, '>Excluir</a>')


# Testes de Validação e persistência de dados
class CriarPessoaPOSTTests(TestCase):
    def test_post_criar_pessoa_campos_obrigatorios_vazios_retorna_erros(self):
        dados = {
            'nome': '',
            'cpf': '',
            'data_nascimento': '',
            'email': ''
        }

        response = self.client.post(reverse('criar_pessoa'), data=dados)

        self.assertEqual(response.status_code, 200)  # Não redireciona
        form = response.context['form']
        self.assertFormError(form, 'nome', 'Este campo é obrigatório.')
        self.assertFormError(form, 'cpf', 'Este campo é obrigatório.')
        self.assertFormError(form, 'data_nascimento', 'Este campo é obrigatório.')
        self.assertFormError(form, 'email', 'Este campo é obrigatório.')

    def test_post_criar_pessoa_com_cpf_invalido_exibe_erro(self):
        dados = {
            'nome': 'Carlos Souza',
            'cpf': '12345678900',  # CPF inválido
            'data_nascimento': '1985-07-22',
            'email': 'carlos@email.com'
        }

        response = self.client.post(reverse('criar_pessoa'), data=dados)

        self.assertEqual(response.status_code, 200)
        form = response.context['form']
        self.assertFormError(form, 'cpf', 'CPF inválido.')

    def test_post_criar_pessoa_com_cpf_duplicado_exibe_erro(self):
        Pessoa.objects.create(
            nome='Carlos Souza',
            cpf='529.982.247-25',
            data_nascimento='1985-07-22',
            email='carlos@email.com'
        )

        dados = {
            'nome': 'Carlos Repetido',
            'cpf': '52998224725',  # Mesma numeração, sem formatação
            'data_nascimento': '1990-01-01',
            'email': 'carlos2@email.com'
        }

        response = self.client.post(reverse('criar_pessoa'), data=dados)

        self.assertEqual(response.status_code, 200)
        form = response.context['form']
        self.assertFormError(form, 'cpf', 'Este CPF já está cadastrado.')

    def test_post_criar_pessoa_com_data_futura_exibe_erro(self):
        dados = {
            'nome': 'Carlos Souza',
            'cpf': '52998224725',
            'data_nascimento': '2100-01-01',
            'email': 'carlos@email.com'
        }

        response = self.client.post(reverse('criar_pessoa'), data=dados)

        self.assertEqual(response.status_code, 200)
        form = response.context['form']
        self.assertFormError(form, 'data_nascimento', 'A data de nascimento não pode ser futura.')

    def test_post_criar_pessoa_com_dados_validos_salva_no_banco(self):
        dados = {
            'nome': 'Maria Oliveira',
            'cpf': '52998224725',
            'data_nascimento': '1992-08-15',
            'email': 'maria@email.com'
        }

        response = self.client.post(reverse('criar_pessoa'), data=dados)

        self.assertEqual(Pessoa.objects.count(), 1)
        pessoa = Pessoa.objects.first()
        self.assertEqual(pessoa.nome, 'Maria Oliveira')
        self.assertEqual(pessoa.cpf, '529.982.247-25')


class EditarPessoaPOSTTests(TestCase):
    def test_post_editar_pessoa_com_dados_validos_atualiza(self):
        pessoa = Pessoa.objects.create(
            nome='Carlos Souza',
            cpf='529.982.247-25',
            data_nascimento='1985-07-22',
            email='carlos@email.com'
        )

        dados = {
            'nome': 'Carlos Atualizado',
            'cpf': '16899554703',  # CPF válido diferente
            'data_nascimento': '1985-07-22',
            'email': 'carlosnovo@email.com'
        }

        response = self.client.post(reverse('editar_pessoa', args=[pessoa.id]), data=dados)

        self.assertEqual(response.status_code, 302)  # redireciona após sucesso
        pessoa_atualizada = Pessoa.objects.get(id=pessoa.id)
        self.assertEqual(pessoa_atualizada.nome, 'Carlos Atualizado')
        self.assertEqual(pessoa_atualizada.cpf, '168.995.547-03')

    def test_post_editar_pessoa_com_data_futura_exibe_erro(self):
        pessoa = Pessoa.objects.create(
            nome='Carlos Souza',
            cpf='529.982.247-25',
            data_nascimento='1985-07-22',
            email='carlos@email.com'
        )

        dados = {
            'nome': 'Carlos Futuro',
            'cpf': '52998224725',
            'data_nascimento': '2100-01-01',
            'email': 'carlos@email.com'
        }

        response = self.client.post(reverse('editar_pessoa', args=[pessoa.id]), data=dados)

        self.assertEqual(response.status_code, 200)
        form = response.context['form']
        self.assertFormError(form, 'data_nascimento', 'A data de nascimento não pode ser futura.')

    def test_post_editar_pessoa_com_cpf_duplicado_exibe_erro(self):
        Pessoa.objects.create(
            nome='Usuário Original',
            cpf='529.982.247-25',
            data_nascimento='1990-01-01',
            email='original@email.com'
        )

        pessoa = Pessoa.objects.create(
            nome='Carlos Souza',
            cpf='168.995.547-03',
            data_nascimento='1985-07-22',
            email='carlos@email.com'
        )

        dados = {
            'nome': 'Carlos Souza',
            'cpf': '52998224725',  # Repetido do primeiro, sem formatação
            'data_nascimento': '1985-07-22',
            'email': 'carlos@email.com'
        }

        response = self.client.post(reverse('editar_pessoa', args=[pessoa.id]), data=dados)

        self.assertEqual(response.status_code, 200)
        form = response.context['form']
        self.assertFormError(form, 'cpf', 'Este CPF já está cadastrado.')


class ExcluirPessoaPOSTTests(TestCase):
    def test_get_excluir_pessoa_exibe_confirmacao(self):
        pessoa = Pessoa.objects.create(
            nome='Carlos Souza',
            cpf='529.982.247-25',
            data_nascimento='1985-07-22',
            email='carlos@email.com'
        )

        response = self.client.get(reverse('excluir_pessoa', args=[pessoa.id]))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Confirmar')

    def test_post_excluir_pessoa_remove_registro(self):
        pessoa = Pessoa.objects.create(
            nome='Carlos Souza',
            cpf='529.982.247-25',
            data_nascimento='1985-07-22',
            email='carlos@email.com'
        )

        self.assertEqual(Pessoa.objects.count(), 1)

        response = self.client.post(reverse('excluir_pessoa', args=[pessoa.id]))

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Pessoa.objects.count(), 0)