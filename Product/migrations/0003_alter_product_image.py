# Generated by Django 3.2.4 on 2021-06-04 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0002_auto_20210604_0806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='product_img/%Y/%m/%d'),
        ),
    ]