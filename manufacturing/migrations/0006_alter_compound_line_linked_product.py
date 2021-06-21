# Generated by Django 3.2.4 on 2021-06-06 10:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manufacturing', '0005_alter_compound_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compound_line',
            name='linked_product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='compound', to='manufacturing.compound'),
        ),
    ]
