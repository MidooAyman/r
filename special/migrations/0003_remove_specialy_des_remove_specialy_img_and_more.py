# Generated by Django 4.1.6 on 2023-04-09 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('special', '0002_rename_name_specialy_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='specialy',
            name='des',
        ),
        migrations.RemoveField(
            model_name='specialy',
            name='img',
        ),
        migrations.RemoveField(
            model_name='specialy',
            name='price',
        ),
        migrations.RemoveField(
            model_name='specialy',
            name='special',
        ),
        migrations.AddField(
            model_name='specialy',
            name='password',
            field=models.CharField(default=2, max_length=100),
            preserve_default=False,
        ),
    ]
