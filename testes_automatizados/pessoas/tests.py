from django.test import TestCase
from django.urls import reverse
from pessoas.models import Pessoa
from django.core.exceptions import ValidationError
from .helpers.validators import validar_cpf

#testes de back end
class ViewsPessoasTests(TestCase):

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
        response = self.client.get(reverse('criar', args=[1]))
        self.assertContains(response, 'type="submit"')
        self.assertContains(response, '>Salvar</button>')


class TesteEditarPessoaView(TestCase):

    def test_editar_pessoa_view_acessada_com_sucesso(self):
        response = self.client.get(reverse('editar_pessoa', args=[1]))
        self.assertEqual(response.status_code, 200)

    def test_editar_pessoa_view_renderiza_template_esperado(self):
        response = self.client.get(reverse('editar_pessoa', args=[1]))
        self.assertTemplateUsed(response, 'pessoas/form.html')

    def test_editar_pessoa_view_renderiza_elemento_log(self):
        response = self.client.get(reverse('editar_pessoa', args=[1]))
        self.assertContains(response, 'VIEW: editar_pessoa')

    def test_editar_pessoa_view_renderiza_formulario(self):
        response = self.client.get(reverse('editar_pessoa', args=[1]))
        self.assertContains(response, '<form')
        self.assertContains(response, '</form>')  

    def test_editar_pessoa_view_exibe_campos_do_formulario(self):
        response = self.client.get(reverse('editar_pessoa', args=[1]))
        self.assertContains(response, 'name="nome"')
        self.assertContains(response, 'name="cpf"')
        self.assertContains(response, 'name="data_nascimento"')
        self.assertContains(response, 'name="email"')

    def test_editar_pessoa_view_renderiza_botao_submit(self):
        response = self.client.get(reverse('editar_pessoa', args=[1]))
        self.assertContains(response, 'type="submit"')
        self.assertContains(response, '>Salvar</button>')


class TesteExcluirPessoaView(TestCase):

    def test_excluir_pessoa_view_acessada_com_sucesso(self):
        response = self.client.get(reverse('excluir_pessoa', args=[1]))
        self.assertEqual(response.status_code, 200)

    def test_excluir_pessoa_view_renderiza_template_esperado(self):
        response = self.client.get(reverse('excluir_pessoa', args=[1]))
        self.assertTemplateUsed(response, 'pessoas/confirmar_exclusao.html')

    def test_excluir_pessoa_view_renderiza_elemento_log(self):
        response = self.client.get(reverse('excluir_pessoa', args=[1]))
        self.assertContains(response, 'VIEW: excluir_pessoa')

    def test_excluir_pessoa_view_renderiza_botao_confirmar(self):
        response = self.client.get(reverse('excluir_pessoa', args=[1]))
        self.assertContains(response, '<form')
        self.assertContains(response, 'type="submit"')
        self.assertContains(response, '>Confirmar</button>')


