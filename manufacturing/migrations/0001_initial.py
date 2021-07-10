# Generated by Django 3.2.4 on 2021-06-06 09:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('list', '0003_alter_target_species_options'),
        ('formulary', '0006_auto_20210606_1921'),
        ('inventory', '0005_alter_packaging_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compound',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, db_index=True, max_length=200, null=True)),
                ('max_qty', models.IntegerField(blank=True, null=True)),
                ('formula_form', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='list.form')),
                ('linked_product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='formulary.formula')),
            ],
            options={
                'ordering': ('name',),
                'index_together': {('id', 'name')},
            },
        ),
        migrations.CreateModel(
            name='Compound_Line',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Amount', models.IntegerField(blank=True, default=0, null=True)),
                ('name', models.CharField(blank=True, db_index=True, default=True, max_length=200)),
                ('UoM', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='list.unit')),
                ('active', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.excipient')),
                ('linked_product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='manufacturing.compound')),
            ],
            options={
                'verbose_name': 'Ingredient',
                'verbose_name_plural': 'Ingredients',
                'ordering': ['linked_product'],
            },
        ),
    ]