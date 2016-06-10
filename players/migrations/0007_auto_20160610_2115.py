# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0006_auto_20160610_2109'),
    ]

    operations = [
        migrations.RenameField(
            model_name='playerdetails',
            old_name='major_style',
            new_name='major_skill',
        ),
        migrations.RenameField(
            model_name='playerdetails',
            old_name='minor_style',
            new_name='minor_skill',
        ),
    ]
