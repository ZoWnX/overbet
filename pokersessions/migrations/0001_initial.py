# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-01 10:26
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('games', '0001_initial'),
        ('locations', '0002_location_created_by'),
    ]

    operations = [
        migrations.CreateModel(
            name='PokerSession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_cash', models.BooleanField(default=True)),
                ('active', models.BooleanField(default=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('deleted', models.BooleanField(default=False)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.Game')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locations.Location')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PokerSessionComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('deleted', models.BooleanField(default=False)),
                ('poker_session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pokersessions.PokerSession')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PokerSessionUpdate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
                ('comment', models.TextField(null=True)),
                ('buy_in', models.DecimalField(decimal_places=2, max_digits=20, null=True)),
                ('chip_stack', models.DecimalField(decimal_places=2, max_digits=20, null=True)),
                ('poker_session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pokersessions.PokerSession')),
            ],
        ),
    ]
