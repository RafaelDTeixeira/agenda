from django.db import models
from django.db.models.fields import DateTimeField

class Evento(models.Model):
    titulo=models.CharField(max_length=100)
    descricao=models.TextField(null=True, blank=True)
    data_evento=DateTimeField(verbose_name='Data do Evento')
    data_criacao=DateTimeField(auto_now=True,verbose_name='Data de Criação')

    class Meta:                 #Alteração do nome da tabela sqlite3: comando sqlmigrate core xxxx/dados para migração manual.
        db_table='evento'

    def __str__(self) -> str:
        return self.titulo

class Pessoa(models.Model):
    nome=models.CharField(max_length=100,null=True)
    idade=models.IntegerField()
    rg=models.CharField(max_length=10)
    endereco=models.TextField(max_length=120,null=True)

    def __str__(self) -> str:
        return self.nome
