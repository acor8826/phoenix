# Generated by Django 3.2.4 on 2021-06-06 02:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0005_alter_packaging_options'),
        ('list', '0003_alter_target_species_options'),
        ('formulary', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='formula',
            options={'ordering': ('name',)},
        ),
        migrations.AddField(
            model_name='formula',
            name='name',
            field=models.CharField(blank=True, db_index=True, max_length=200, null=True),
        ),
        migrations.CreateModel(
            name='Formula_Line',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('strength', models.IntegerField(blank=True, default=0, null=True)),
                ('name', models.CharField(blank=True, db_index=True, default=True, max_length=200)),
                ('UoM', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='list.unit')),
                ('active', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.active')),
                ('linked_product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='formulary.formula')),
            ],
            options={
                'ordering': ['linked_product'],
            },
        ),
    ]
