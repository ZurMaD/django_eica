# Generated by Django 3.0.2 on 2020-01-29 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eica', '0002_platohijoventa_cantidad'),
    ]

    operations = [
        migrations.AddField(
            model_name='boletaventarestaurante',
            name='cliente',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
