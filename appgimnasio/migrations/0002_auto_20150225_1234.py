# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appgimnasio', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gasto',
            name='codigo',
        ),
        migrations.RemoveField(
            model_name='ingreso',
            name='codigo',
        ),
        migrations.RemoveField(
            model_name='servicio',
            name='codigo',
        ),
        migrations.AddField(
            model_name='gasto',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, default=1, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ingreso',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, default=1, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='servicio',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, default=1, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
