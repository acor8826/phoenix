# Generated by Django 3.2.4 on 2021-06-06 02:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_alter_excipient_is_active'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='packaging',
            options={'ordering': ('pack_desc',), 'verbose_name': 'Packaging', 'verbose_name_plural': 'Packaging'},
        ),
    ]