# Generated by Django 3.2.4 on 2021-06-06 09:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manufacturing', '0002_alter_compound_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='compound',
            old_name='max_qty',
            new_name='qty_to_make',
        ),
    ]
