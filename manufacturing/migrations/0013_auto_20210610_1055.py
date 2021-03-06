# Generated by Django 3.2.4 on 2021-06-10 00:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0003_alter_target_species_options'),
        ('manufacturing', '0012_auto_20210610_0947'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compound',
            name='instruction',
        ),
        migrations.CreateModel(
            name='Compound_Instruction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('step_no', models.IntegerField(blank=True, default=0, null=True)),
                ('name', models.CharField(blank=True, db_index=True, default=True, max_length=200)),
                ('instruction_form', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='list.form')),
                ('linked_product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='manufacturing.compound')),
            ],
            options={
                'verbose_name': 'Instruction',
                'verbose_name_plural': 'Instructions',
                'ordering': ['step_no'],
            },
        ),
    ]
