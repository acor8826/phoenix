# Generated by Django 3.2.4 on 2021-06-10 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formulary', '0018_alter_instruction_step_step_no'),
    ]

    operations = [
        migrations.RenameField(
            model_name='instruction_step',
            old_name='linked_instruction',
            new_name='linked_instruction_step',
        ),
        migrations.RemoveField(
            model_name='instruction',
            name='linked_product',
        ),
        migrations.AddField(
            model_name='formula',
            name='instruction',
            field=models.ManyToManyField(blank=True, to='formulary.Instruction'),
        ),
    ]
