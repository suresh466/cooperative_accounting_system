from django.db import models

# Create your models here.

class MainAccount(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255)
    code = models.FloatField()

    def __str__(self):
        return str(self.code) + " / " + self.name

class SecondaryAccount(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True)
    main_account = models.ForeignKey(MainAccount, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    code = models.FloatField()

    def __str__(self):
        return str(self.code) + " / " + self.name

class PersonalAccount(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    code = models.FloatField()

    def __str__(self):
        return str(self.code) + " / " + self.name
