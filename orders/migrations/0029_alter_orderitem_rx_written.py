# Generated by Django 3.2.4 on 2021-06-20 01:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0028_alter_orderitem_rx_written'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='rx_written',
            field=models.DateField(blank=True, default=datetime.date.today, null=True),
        ),
    ]
