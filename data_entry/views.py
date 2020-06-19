from django.shortcuts import render
# Create your views here.

def data_entry(request):
    template = 'data_entry/data_entry.html'

    return render(request, template)
