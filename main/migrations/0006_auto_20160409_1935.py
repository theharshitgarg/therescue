# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20160409_1930'),
    ]

    operations = [
        migrations.AddField(
            model_name='rescueoperation',
            name='closed_on',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 9, 19, 35, 7, 361393, tzinfo=utc), verbose_name=b'closed_on'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rescueoperation',
            name='started_on',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 9, 19, 35, 18, 539646, tzinfo=utc), verbose_name=b'started_on'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='animal',
            name='found_on',
            field=models.DateTimeField(verbose_name=b'found_on'),
        ),
    ]
