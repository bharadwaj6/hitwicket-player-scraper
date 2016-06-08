# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0004_auto_20160602_1959'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlayerTypeDetails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('player_id', models.IntegerField(null=True)),
                ('region', models.CharField(max_length=255)),
                ('skill_index', models.IntegerField()),
                ('main_skill_type', models.CharField(max_length=255)),
                ('sub_skill_type', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
