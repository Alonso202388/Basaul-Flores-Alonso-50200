# Generated by Django 4.2.4 on 2024-03-19 05:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('BasaulApp', '0004_rename_estudiante_id_entregable_estudiante'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='estudiante',
            options={},
        ),
        migrations.AlterModelOptions(
            name='profesor',
            options={},
        ),
        migrations.AddField(
            model_name='estudiante',
            name='cursos',
            field=models.ManyToManyField(to='BasaulApp.curso'),
        ),
        migrations.AddField(
            model_name='estudiante',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='profesor',
            name='cursos',
            field=models.ManyToManyField(to='BasaulApp.curso'),
        ),
        migrations.AddField(
            model_name='profesor',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
