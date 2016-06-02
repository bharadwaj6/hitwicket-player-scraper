# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0003_divteamdetails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playerdetails',
            name='player_id',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
    ]
