from django.test import TestCase
from .forms import ListaPresencaForm

class ListaPresencaFormTest(TestCase):
    def test_form_valid_data(self):
        form_data = {
            'nome': 'João',
            'nome_professor': 'Orlando',
            'disciplina': 'SI',
        }
        form = ListaPresencaForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_invalid_data(self):
        form_data = {
            'nome': '',
            'nome_professor': 'Orlando',
            'disciplina': 'SI',
        }
        form = ListaPresencaForm(data=form_data)
        self.assertFalse(form.is_valid())
