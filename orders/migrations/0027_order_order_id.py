# Generated by Django 3.2.4 on 2021-06-19 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0026_orderitem_rx_written'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
