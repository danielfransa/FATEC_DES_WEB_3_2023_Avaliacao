from django import forms
from .models import ListaPresenca

class ListaPresencaForm(forms.ModelForm):
    class Meta:
        model = ListaPresenca
        fields = ['nome', 'nome_professor', 'disciplina']