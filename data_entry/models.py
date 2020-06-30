from django.db import models
from accounts.models import (MainAccount, SecondaryAccount,
        PersonalAccount,)
# Create your models here.

class EntryBundle(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.date_created

class Entry(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    count = models.PositiveIntegerField()
    entry_bundle = models.ForeignKey(EntryBundle, on_delete=models.CASCADE)
    main_account = models.ForeignKey(MainAccount, on_delete=models.DO_NOTHING)
    secondary_account = models.ForeignKey(SecondaryAccount, on_delete=models.DO_NOTHING)
    personal_account = models.ForeignKey(PersonalAccount, on_delete=models.DO_NOTHING)
    amount = models.DecimalField(max_digits=11, decimal_places=2)

    def __str__(self):
        return self.date_created

