from django.urls import path
from .views import data_entry

app_name = 'data_entry'
urlpatterns = [
        path('', data_entry, name='data_entry'),
        ]
