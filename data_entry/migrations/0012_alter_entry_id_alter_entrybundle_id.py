# Generated by Django 4.0.3 on 2022-03-27 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_entry', '0011_auto_20200725_1048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='entrybundle',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
