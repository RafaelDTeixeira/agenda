# Generated by Django 4.0.1 on 2022-01-12 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_evento_local_alter_evento_data_criacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='local',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]