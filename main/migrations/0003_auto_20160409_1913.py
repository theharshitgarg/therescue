# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20160409_1820'),
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.CharField(max_length=50)),
                ('found_at', models.CharField(max_length=50)),
                ('found_on', models.CharField(max_length=50)),
                ('is_injured', models.BooleanField(default=False)),
                ('is_handicapped', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='RescueOperation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('started_at', models.CharField(max_length=200)),
                ('started_by', models.CharField(max_length=200)),
                ('closed_at', models.CharField(max_length=200)),
                ('treated_at', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='rescuer',
            name='no_of_animals_rescued',
            field=models.IntegerField(default=0),
        ),
    ]
