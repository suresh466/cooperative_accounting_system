from django.urls import path
from .views import data_entry, load_secondary_accounts, get_entry

app_name = 'data_entry'
urlpatterns = [
        path('', data_entry, name='data_entry'),
        path('ajax/load_secondary_accounts/', load_secondary_accounts, name='ajax_load_secondary_accounts'),
        path('ajax/get_entry/', get_entry, name='get_entry'),
        ]
