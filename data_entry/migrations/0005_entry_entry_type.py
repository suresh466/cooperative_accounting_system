# Generated by Django 3.0.7 on 2020-07-02 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_entry', '0004_auto_20200630_1704'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='entry_type',
            field=models.CharField(choices=[('dr', 'Dr'), ('cr', 'Cr')], default='Dr', max_length=2),
            preserve_default=False,
        ),
    ]