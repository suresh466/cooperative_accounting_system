# Generated by Django 3.0.7 on 2020-06-30 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data_entry', '0002_auto_20200630_1201'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entrybundle',
            name='code',
        ),
    ]