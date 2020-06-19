from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def data_entry(request):
    return HttpResponse("data-entry view")
