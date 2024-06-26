# Generated by Django 4.1.6 on 2023-04-09 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('special', '0003_remove_specialy_des_remove_specialy_img_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='specialy',
            old_name='password',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='specialy',
            name='username',
        ),
        migrations.AddField(
            model_name='specialy',
            name='des',
            field=models.TextField(default=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='specialy',
            name='img',
            field=models.ImageField(default=10, upload_to='pics'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='specialy',
            name='price',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='specialy',
            name='special',
            field=models.BooleanField(default=False),
        ),
    ]
