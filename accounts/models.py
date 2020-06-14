from django.db import models

# Create your models here.

class MainAccount(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255)
    code = models.FloatField(max_length=255)

class SecondaryAccount(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True)
    main_account = models.ForeignKey(MainAccount, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    code = models.FloatField(max_length=255)
