from django.db import models

PROFESSORES = [
    ('Orlando', 'Orlando'),
    ('Nilton', 'Nilton'),
    ('Thiago', 'Thiago'),
    ('Dhebora', 'Dhebora'),
    ('Amanda', 'Amanda'),
    ('Marcelo', 'Marcelo'),
]

DISCIPLINAS = [
    ('DSM', 'Desenvolvimento de Software Multilataforma'),
    ('GE', 'Gestão Empresarial'),
    ('SI', 'Sistemas para Internet'),
]


class ListaPresenca(models.Model):
    nome = models.CharField('Nome Aluno', max_length=100)
    nome_professor = models.CharField('Nome Professor', max_length=50, choices=PROFESSORES)
    disciplina = models.CharField('Disciplina', max_length=20, choices=DISCIPLINAS)
    
    
