# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('identificacion', models.IntegerField(serialize=False, verbose_name=b'Numero de Documento', primary_key=True)),
                ('nombre', models.CharField(max_length=b'50', verbose_name=b'Primer Nombre')),
                ('segundoNombre', models.CharField(max_length=b'50', null=True, verbose_name=b'Segundo Nombre')),
                ('apellido', models.CharField(max_length=b'50', verbose_name=b'Primer Apellido')),
                ('segundoApellido', models.CharField(max_length=b'50', null=True, verbose_name=b'Segundo Apellido')),
                ('fechaNacimiento', models.DateField(verbose_name=b'Fecha de Nacimiento')),
                ('telefono', models.CharField(max_length=b'10', verbose_name=b'Telefono')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ConceptoGasto',
            fields=[
                ('codigo', models.CharField(max_length=b'5', serialize=False, verbose_name=b'Codigo', primary_key=True)),
                ('nombre', models.CharField(max_length=b'30', verbose_name=b'Nombre del Concepto')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ConceptoIngreso',
            fields=[
                ('codigo', models.CharField(max_length=b'5', serialize=False, verbose_name=b'Codigo', primary_key=True)),
                ('nombre', models.CharField(max_length=b'30', verbose_name=b'Nombre del Concepto')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('identificacion', models.IntegerField(max_length=b'20', serialize=False, verbose_name=b'Numero de Documento', primary_key=True)),
                ('nombre', models.CharField(max_length=b'50', verbose_name=b'Primer Nombre')),
                ('segundoNombre', models.CharField(max_length=b'50', null=True, verbose_name=b'Segundo Nombre')),
                ('apellido', models.CharField(max_length=b'50', verbose_name=b'Primer Apellido')),
                ('segundoApellido', models.CharField(max_length=b'50', null=True, verbose_name=b'Segundo Apellido')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Gasto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField(auto_now=True, verbose_name=b'Fecha')),
                ('monto', models.IntegerField(max_length=b'6')),
                ('concepto', models.ForeignKey(to='appgimnasio.ConceptoGasto')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Gimnasio',
            fields=[
                ('codigo', models.CharField(max_length=b'5', serialize=False, verbose_name=b'Codigo', primary_key=True)),
                ('nombre', models.CharField(max_length=b'70', verbose_name=b'Nombre Gimnasio')),
                ('direccion', models.CharField(max_length=b'30', verbose_name=b'Direccion')),
                ('telefono', models.CharField(max_length=b'10', verbose_name=b'Telefono')),
                ('correo', models.EmailField(max_length=75)),
                ('urlfacebook', models.URLField(null=True, blank=True)),
                ('urltwitter', models.URLField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HistorialIngresoCliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateTimeField(verbose_name=b'Fecha')),
                ('idCliente', models.ForeignKey(to='appgimnasio.Cliente')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Ingreso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField(auto_now=True, verbose_name=b'Fecha')),
                ('monto', models.IntegerField(max_length=b'6')),
                ('concepto', models.ForeignKey(to='appgimnasio.ConceptoIngreso')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('servicio', models.CharField(max_length=50, verbose_name=b'Servicio')),
                ('tarifa', models.IntegerField(max_length=b'6')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
