# Generated by Django 5.1.1 on 2024-10-09 02:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PlanLab', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='aula',
            name='avaliacao_observacoes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='aula',
            name='eventos_extraordinarios',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='aula',
            name='observacoes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='aula',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
