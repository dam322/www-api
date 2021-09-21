# Generated by Django 3.2.7 on 2021-09-21 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='is_available',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ingredient',
            name='is_obligatory',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
