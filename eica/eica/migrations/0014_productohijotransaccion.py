# Generated by Django 3.0.1 on 2020-01-31 19:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eica', '0013_boletaventarestaurante_vendedor'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductoHijoTransaccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.FloatField(blank=True, null=True)),
                ('fecha_transsacion', models.DateTimeField(blank=True, null=True)),
                ('fecha_creado', models.DateTimeField(blank=True, null=True)),
                ('fecha_modificado', models.DateTimeField(blank=True, null=True)),
                ('producto_padre', models.ForeignKey(blank=True, db_column='id_producto_padre', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='eica.ProductoPadre')),
            ],
            options={
                'db_table': 'producto_hijo_transaccion',
                'managed': True,
            },
        ),
    ]
