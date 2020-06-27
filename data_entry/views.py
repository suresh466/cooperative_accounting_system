from django.shortcuts import render
from .forms import DataEntryForm
from accounts.models import SecondaryAccount
from django.http import HttpResponse
# Create your views here.

def data_entry(request):
    template = 'data_entry/data_entry.html'

    if 'done' in request.POST:
        print(".........indide done") #sanity check

    form = DataEntryForm()

    context = {
            'form': form,
            }

    return render(request, template, context)

def load_secondary_accounts(request):
    template = 'data_entry/secondary_account_dropdown_list_options.html'

    main_account_id = request.GET.get('main_account')
    secondary_accounts = SecondaryAccount.objects.filter(main_account_id = main_account_id).order_by('code')

    context = {
            'secondary_accounts': secondary_accounts,
            }

    return render(request, template, context)

def get_entry(request):

    main_account = request.POST['main_account']
    secondary_account = request.POST['secondary_account']
    personal_account = request.POST.get('personal_account')
    amount = request.POST['amount']

    print(main_account)
    print(secondary_account)
    print(personal_account)
    print(amount)

    return HttpResponse('')
