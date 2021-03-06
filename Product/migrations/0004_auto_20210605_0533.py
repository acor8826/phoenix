# Generated by Django 3.2.4 on 2021-06-04 19:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0001_initial'),
        ('inventory', '0001_initial'),
        ('Product', '0003_alter_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sales_Packaging',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_desc', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='form',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='list.form'),
        ),
        migrations.CreateModel(
            name='Product_Line',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('strength', models.IntegerField(blank=True, default=0, null=True)),
                ('name', models.CharField(blank=True, db_index=True, default=True, max_length=200)),
                ('UoM', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='list.unit')),
                ('active', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.active')),
                ('linked_product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Product.product')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='packaging',
            field=models.ManyToManyField(blank=True, to='Product.Sales_Packaging'),
        ),
    ]
