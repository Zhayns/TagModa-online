# Generated by Django 4.0 on 2022-04-06 22:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_contacto'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contacto',
            old_name='nomrbe',
            new_name='nombreContacto',
        ),
    ]
