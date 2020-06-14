from django.contrib import admin
from .models import MainAccount, SecondaryAccount
# Register your models here.

admin.site.register(MainAccount)
admin.site.register(SecondaryAccount)
