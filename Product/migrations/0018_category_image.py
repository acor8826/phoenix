# Generated by Django 3.2.4 on 2021-06-30 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0017_alter_sales_packaging_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, upload_to='category_img/%Y/%m/%d'),
        ),
    ]
