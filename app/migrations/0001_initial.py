# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('email', models.EmailField(unique=True, max_length=254)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50, null=True, blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('provider', models.CharField(default=b'Local', max_length=15, choices=[(b'Local', b'Local'), (b'Facebook', b'Facebook')])),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Event_Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Event_Type',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(default=b'')),
                ('date', models.DateField()),
                ('place', models.TextField()),
                ('time', models.TimeField()),
                ('price', models.DecimalField(max_digits=5, decimal_places=2)),
                ('category', models.ForeignKey(to='app.Event_Category')),
                ('event_type', models.ForeignKey(to='app.Event_Type')),
            ],
        ),
        migrations.CreateModel(
            name='Organizations',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(default=b'')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('premium', models.BooleanField(default=False)),
                ('premium_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('owner', models.OneToOneField(primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('facebook_id', models.CharField(max_length=20, unique=True, null=True, blank=True)),
                ('facebook_token', models.CharField(max_length=1000, unique=True, null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='organizations',
            name='user',
            field=models.ForeignKey(related_name='orgs', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='events',
            name='organization',
            field=models.ForeignKey(related_name='org_events', blank=True, to='app.Organizations', null=True),
        ),
        migrations.AddField(
            model_name='events',
            name='user',
            field=models.ForeignKey(related_name='user_events', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='organizations',
            unique_together=set([('name', 'premium')]),
        ),
    ]
