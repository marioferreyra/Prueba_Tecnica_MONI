# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-11-06 22:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pedido_prestamo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prestamo',
            old_name='monto_solicitado',
            new_name='monto',
        ),
    ]