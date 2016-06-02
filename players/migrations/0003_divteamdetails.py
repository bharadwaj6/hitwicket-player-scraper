# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0002_playerdetails_team_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='DivTeamDetails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('team_id', models.IntegerField()),
                ('div_id', models.IntegerField()),
                ('league_id', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
