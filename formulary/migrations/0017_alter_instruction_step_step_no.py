# Generated by Django 3.2.4 on 2021-06-10 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formulary', '0016_auto_20210610_2024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instruction_step',
            name='step_no',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='subs-step'),
        ),
    ]
