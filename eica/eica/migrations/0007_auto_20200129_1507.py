# Generated by Django 3.0.1 on 2020-01-29 20:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eica', '0006_boletacompra_valido'),
    ]

    operations = [
        migrations.RenameField(
            model_name='boletacompra',
            old_name='fecha_modifcado',
            new_name='fecha_modificado',
        ),
    ]
