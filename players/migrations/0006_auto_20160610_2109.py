# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0005_playertypedetails'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PlayerTypeDetails',
        ),
        migrations.AddField(
            model_name='playerdetails',
            name='major_style',
            field=models.CharField(max_length=255, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='playerdetails',
            name='minor_style',
            field=models.CharField(max_length=255, null=True),
            preserve_default=True,
        ),
    ]
