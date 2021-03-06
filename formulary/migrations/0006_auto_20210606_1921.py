# Generated by Django 3.2.4 on 2021-06-06 09:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formulary', '0005_rename_strength_formula_line_amount'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='formula_line',
            options={'ordering': ['linked_product'], 'verbose_name': 'Ingredient', 'verbose_name_plural': 'Ingredients'},
        ),
        migrations.AlterIndexTogether(
            name='formula',
            index_together={('id', 'name')},
        ),
    ]
