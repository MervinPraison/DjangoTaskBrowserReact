# Generated by Django 2.2.5 on 2019-09-24 00:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('browser', '0007_auto_20190923_2254'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={},
        ),
        migrations.AlterUniqueTogether(
            name='task',
            unique_together=set(),
        ),
    ]
