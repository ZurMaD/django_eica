# Generated by Django 3.0.1 on 2019-12-31 00:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('eica', '0006_auto_20191231_0006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personas',
            name='fecha_creado',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2019, 12, 31, 0, 15, 10, 924714, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
