# Generated by Django 3.2.4 on 2021-06-06 00:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('formulary', '0001_initial'),
        ('Product', '0015_remove_product_compound'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='formula',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='formula', to='formulary.formula'),
        ),
    ]
