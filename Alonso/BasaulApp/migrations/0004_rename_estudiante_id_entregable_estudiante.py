# Generated by Django 4.2.4 on 2024-03-19 04:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BasaulApp', '0003_remove_entregable_estudiante_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entregable',
            old_name='estudiante_id',
            new_name='estudiante',
        ),
    ]
