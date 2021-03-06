# Generated by Django 3.2.4 on 2021-06-08 00:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_clinic'),
        ('orders', '0005_order_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='client',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.clinic'),
        ),
        migrations.AlterField(
            model_name='client',
            name='customer',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.customer'),
        ),
    ]
