# Generated by Django 3.2.4 on 2021-06-13 06:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0024_auto_20210613_1640'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={},
        ),
        migrations.RemoveField(
            model_name='customer',
            name='user',
        ),
    ]
