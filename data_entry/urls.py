from django.urls import path
from .views import (data_entry, load_secondary_accounts,
        get_entry, discard_session_entry,
        save_session_entries, cancel_session_entries,)

app_name = 'data_entry'
urlpatterns = [
        path('', data_entry, name='data_entry'),
        path('ajax/load_secondary_accounts/', load_secondary_accounts, name='ajax_load_secondary_accounts'),
        path('ajax/get_entry/', get_entry, name='get_entry'),
        path('ajax/discard_session_entry/', discard_session_entry, name='discard_session_entry'),
        path('ajax/discard_session_entry/', discard_session_entry, name='discard_session_entry'),
        path('ajax/save_session_entries/', save_session_entries, name='save_session_entries'),
        path('ajax/cancel_session_entries/', cancel_session_entries, name='cancel_session_entries'),
        ]
