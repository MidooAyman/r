# Generated by Django 4.1.6 on 2023-04-10 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='pics')),
                ('des', models.TextField()),
                ('price', models.IntegerField()),
                ('special', models.BooleanField(default=False)),
            ],
        ),
    ]
