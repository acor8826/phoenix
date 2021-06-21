# Generated by Django 3.2.4 on 2021-06-09 23:39

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0003_alter_target_species_options'),
        ('manufacturing', '0010_compound_line_weighed'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compounding_Instruction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('step_no', models.IntegerField(blank=True, default=0, null=True)),
                ('name', models.CharField(blank=True, db_index=True, default=True, max_length=200)),
                ('Instruction_form', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='list.form')),
                ('linked_product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='manufacturing.compound')),
            ],
            options={
                'verbose_name': 'Instruction',
                'verbose_name_plural': 'Instructions',
                'ordering': ['step_no'],
            },
        ),
        migrations.CreateModel(
            name='Compound_Instruction_Step',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('step_no', models.IntegerField(blank=True, default=0, null=True)),
                ('ix', ckeditor.fields.RichTextField(default=True, verbose_name='Instruction')),
                ('linked_compound_instruction_line', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='manufacturing.compounding_instruction')),
            ],
            options={
                'verbose_name': 'Process Step',
                'verbose_name_plural': 'Process Steps',
                'ordering': ['step_no'],
            },
        ),
    ]
