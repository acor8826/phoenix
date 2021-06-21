# Generated by Django 3.2.4 on 2021-06-09 02:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0022_auto_20210609_1206'),
        ('orders', '0011_alter_orderitem_shipping_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='shippingaddress',
            name='customer',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.customer'),
        ),
    ]
