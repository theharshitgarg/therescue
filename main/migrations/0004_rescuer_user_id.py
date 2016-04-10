# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20160409_1913'),
    ]

    operations = [
        migrations.AddField(
            model_name='rescuer',
            name='user_id',
            field=models.CharField(default='sdf', max_length=100),
            preserve_default=False,
        ),
    ]
