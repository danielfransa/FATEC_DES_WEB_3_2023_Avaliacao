from django.test import TestCase
from .forms import ListaPresencaForm

class InitialTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/')
    
    def test_200_response(self):
        self.assertEqual(200, self.resp.status_code)

class CadastroTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/lista')
    
    def test_200_response(self):
        self.assertEqual(200, self.resp.status_code)

class ListaPresencaFormTest(TestCase):
    def test_form_valid_data(self):
        form_data = {
            'nome': 'João',
            'nome_professor': 'Orlando',
            'disciplina': 'SI',
        }
        form = ListaPresencaForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_invalid_data_name(self):
        form_data = {
            'nome': '',
            'nome_professor': 'Orlando',
            'disciplina': 'SI',
        }
        form = ListaPresencaForm(data=form_data)
        self.assertFalse(form.is_valid())
    
    def test_form_invalid_data_name_professor(self):
        form_data = {
            'nome': 'Pedro',
            'nome_professor': '',
            'disciplina': 'SI',
        }
        form = ListaPresencaForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_form_invalid_data_disciplina(self):
        form_data = {
            'nome': 'Pedro',
            'nome_professor': 'Orlando',
            'disciplina': '',
        }
        form = ListaPresencaForm(data=form_data)
        self.assertFalse(form.is_valid())
