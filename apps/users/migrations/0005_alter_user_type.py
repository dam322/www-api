# Generated by Django 3.2.7 on 2021-09-28 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='type',
            field=models.CharField(choices=[('admin', 'Admin'), ('employee', 'Employee'), ('customer', 'Customer')], default='customer', max_length=16),
        ),
    ]