# Generated by Django 3.2.4 on 2021-06-09 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0014_auto_20210609_1434'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='tot_cost',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
