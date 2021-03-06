# Generated by Django 3.0.8 on 2020-08-02 10:01

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='as_actor',
        ),
        migrations.RemoveField(
            model_name='person',
            name='as_director',
        ),
        migrations.RemoveField(
            model_name='person',
            name='as_producer',
        ),
        migrations.AddField(
            model_name='movie',
            name='cast',
            field=models.ManyToManyField(related_name='as_actor', related_query_name='actor', to='api.Person'),
        ),
        migrations.AddField(
            model_name='movie',
            name='directors',
            field=models.ManyToManyField(related_name='as_director', related_query_name='director', to='api.Person'),
        ),
        migrations.AddField(
            model_name='movie',
            name='producers',
            field=models.ManyToManyField(related_name='as_producers', related_query_name='producer', to='api.Person'),
        ),
        migrations.AlterField(
            model_name='person',
            name='aliases',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=256), null=True, size=None),
        ),
    ]
