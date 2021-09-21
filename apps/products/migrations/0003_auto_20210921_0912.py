# Generated by Django 3.2.7 on 2021-09-21 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20210920_2142'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Option',
            new_name='Variation',
        ),
        migrations.AddField(
            model_name='product',
            name='is_available',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]