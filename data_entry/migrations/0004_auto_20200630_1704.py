# Generated by Django 3.0.7 on 2020-06-30 17:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data_entry', '0003_remove_entrybundle_code'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entry',
            old_name='code',
            new_name='count',
        ),
    ]
