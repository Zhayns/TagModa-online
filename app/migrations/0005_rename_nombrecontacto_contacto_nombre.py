# Generated by Django 4.0 on 2022-04-06 22:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_rename_nomrbe_contacto_nombrecontacto'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contacto',
            old_name='nombreContacto',
            new_name='nombre',
        ),
    ]
