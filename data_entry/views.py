from django.shortcuts import render, redirect
from .forms import DataEntryForm
from accounts.models import (MainAccount, SecondaryAccount,
        PersonalAccount)
from django.http import HttpResponse
from .models import EntryBundle, Entry
# Create your views here.

def data_entry(request):
    template = 'data_entry/data_entry.html'

    entrybundle = EntryBundle(code= 0)

    if 'done' in request.POST:
        if request.session['entries']:
            entrybundle.save()
        for entry in request.session['entries']:
            ma_pk = entry['ma']
            sa_pk = entry['sa']
            pa_pk = entry['pa']

            ma = MainAccount.objects.get(pk=ma_pk)
            sa = SecondaryAccount.objects.get(pk=ma_pk)
            pa = PersonalAccount.objects.get(pk=ma_pk)
            a = entry['a']

            entry = Entry(main_account=ma, secondary_account=sa, personal_account=pa, amount=a, entry_bundle_code=entrybundle, code=0)
            entry.save()

        del request.session['entries']
        return redirect('data_entry:data_entry')

    request.session['entries'] = [] #create or overwrite if already exists

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

    entry = {'ma': main_account, 'sa': secondary_account, 'pa': personal_account, 'a': amount}
    request.session['entries'].append(entry)
    request.session.modified = True

    return HttpResponse('')
