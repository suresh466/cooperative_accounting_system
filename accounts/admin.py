from django.contrib import admin
from .models import (MainAccount, SecondaryAccount,
        PersonalAccount,)
# Register your models here.

admin.site.register(MainAccount)
admin.site.register(SecondaryAccount)
admin.site.register(PersonalAccount)
