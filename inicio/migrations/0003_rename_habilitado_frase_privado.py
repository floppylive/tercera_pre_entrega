# Generated by Django 4.1.7 on 2023-04-08 17:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0002_frase_rename_persona_moderador_delete_animal_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='frase',
            old_name='habilitado',
            new_name='privado',
        ),
    ]
