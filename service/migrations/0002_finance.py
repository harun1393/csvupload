# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Finance',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('product_name', models.CharField(max_length=150)),
                ('price', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
