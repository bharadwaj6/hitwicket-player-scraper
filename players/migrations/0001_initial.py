# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PlayerDetails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('age', models.CharField(max_length=12, null=True)),
                ('name', models.CharField(max_length=1024, null=True)),
                ('player_id', models.IntegerField()),
                ('region', models.CharField(max_length=255)),
                ('skill_index', models.IntegerField()),
                ('exp', models.CharField(max_length=255)),
                ('form', models.CharField(max_length=23)),
                ('fitness', models.CharField(max_length=255)),
                ('salary', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
