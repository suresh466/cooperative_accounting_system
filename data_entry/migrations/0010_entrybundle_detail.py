# Generated by Django 3.0.7 on 2020-07-20 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_entry', '0009_remove_entrybundle_detail'),
    ]

    operations = [
        migrations.AddField(
            model_name='entrybundle',
            name='detail',
            field=models.TextField(default='nothing', max_length=1536),
            preserve_default=False,
        ),
    ]