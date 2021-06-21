# Generated by Django 3.2.4 on 2021-06-10 03:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manufacturing', '0015_rename_instruction_step_compounding_instruction_step'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compounding_instruction_step',
            name='linked_instruction',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Compound_Instruction', to='manufacturing.compound_instruction'),
        ),
    ]
