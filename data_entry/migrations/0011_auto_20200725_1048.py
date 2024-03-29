# Generated by Django 3.0.7 on 2020-07-25 10:48

from decimal import Decimal
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_entry', '0010_entrybundle_detail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=11, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))]),
        ),
    ]
