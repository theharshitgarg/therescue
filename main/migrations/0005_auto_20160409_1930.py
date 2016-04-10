# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_rescuer_user_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rescueoperation',
            name='id',
        ),
        migrations.AddField(
            model_name='rescueoperation',
            name='rescue_id',
            field=models.IntegerField(default=1, serialize=False, primary_key=True),
            preserve_default=False,
        ),
    ]
