# Generated by Django 3.0.7 on 2020-06-30 12:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data_entry', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entry',
            old_name='entry_bundle_code',
            new_name='entry_bundle',
        ),
    ]
