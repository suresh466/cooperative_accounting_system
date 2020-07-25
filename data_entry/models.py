from django.db import models
from accounts.models import (MainAccount, SecondaryAccount,
        PersonalAccount,)
from django.core.validators import MinValueValidator
from decimal import Decimal
# Create your models here.


class EntryBundle(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, editable=False)
    date_updated = models.DateTimeField(auto_now=True, editable=False)
    detail = models.TextField(max_length=1536)

    def __str__(self):
        return str(self.date_created)

class Entry(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, editable=False)
    date_updated = models.DateTimeField(auto_now=True, editable=False)
    count = models.PositiveIntegerField()
    entry_bundle = models.ForeignKey(EntryBundle, on_delete=models.CASCADE)
    main_account = models.ForeignKey(MainAccount, on_delete=models.DO_NOTHING)
    secondary_account = models.ForeignKey(SecondaryAccount, on_delete=models.DO_NOTHING)
    personal_account = models.ForeignKey(PersonalAccount, on_delete=models.DO_NOTHING)
    symbol_number = models.PositiveIntegerField()
    amount = models.DecimalField(max_digits=11, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])
    DEBIT = 'dr'
    CREDIT = 'cr'
    ENTRY_TYPE_CHOICE = (
            (DEBIT, 'Dr'),
            (CREDIT, 'Cr')
            )
    entry_type = models.CharField(choices=ENTRY_TYPE_CHOICE, max_length=2)

    def __str__(self):
        return str(self.date_created)

