# Generated by Django 3.2.4 on 2021-07-10 08:58

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0018_category_image'),
        ('orders', '0031_alter_orderitem_packaging'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='packaging',
            field=smart_selects.db_fields.ChainedForeignKey(blank=True, chained_field='packaging', chained_model_field='product', null=True, on_delete=django.db.models.deletion.CASCADE, to='Product.product', verbose_name='Sales Packaging'),
        ),
    ]