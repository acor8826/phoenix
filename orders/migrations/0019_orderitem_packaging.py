# Generated by Django 3.2.4 on 2021-06-09 09:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0017_alter_sales_packaging_options'),
        ('orders', '0018_orderitem_doctor'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='packaging',
            field=models.OneToOneField(blank=True, default=True, on_delete=django.db.models.deletion.CASCADE, to='Product.sales_packaging'),
        ),
    ]
