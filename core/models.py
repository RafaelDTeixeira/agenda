from django.db import models
from django.db.models.fields import DateTimeField
from django.contrib.auth.models import User

class Evento(models.Model):
    titulo=models.CharField(max_length=100)
    descricao=models.TextField(null=True, blank=True)
    data_evento=DateTimeField(verbose_name='Data do Evento')
    data_criacao=DateTimeField(auto_now=True,verbose_name='Data de Criacao')
    usuario=models.ForeignKey(User,on_delete=models.CASCADE) # models.cascade (Se o usuário for deletado, seus eventos também serão.) Para User será necessário defenir um valor padrão.

    class Meta:                 #Alteração do nome da tabela sqlite3: comando sqlmigrate core xxxx/dados para migração manual.
        db_table='evento'

    def __str__(self) -> str:
        return self.titulo

    def get_data_evento(self):
        return self.data_evento.strftime('%d/%m/%y %H:%M')

