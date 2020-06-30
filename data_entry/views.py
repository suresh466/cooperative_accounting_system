from django.shortcuts import render, redirect
from .forms import DataEntryForm
from accounts.models import (MainAccount, SecondaryAccount,
        PersonalAccount)
from django.http import JsonResponse, HttpResponse
from .models import EntryBundle, Entry
# Create your views here.

def data_entry(request):
    template = 'data_entry/data_entry.html'

    entrybundle = EntryBundle()

    if request.method == "POST":

        if 'done' in request.POST:
            if request.session['entries']:
                entrybundle.save()
                counter = 0
                for entry in request.session['entries']:
                    ma_pk = entry['ma']
                    sa_pk = entry['sa']
                    pa_pk = entry['pa']

                    ma = MainAccount.objects.get(pk=ma_pk)
                    sa = SecondaryAccount.objects.get(pk=sa_pk)
                    pa = PersonalAccount.objects.get(pk=pa_pk)
                    a = entry['a']
                    counter += 1

                    entry = Entry(main_account=ma, secondary_account=sa, personal_account=pa, amount=a, entry_bundle=entrybundle, count=counter)
                    entry.save()

                del request.session['entries']

        elif 'discard' in request.POST:
            if request.session['entries']:
                del request.session['entries']
            else:
                print('No entries in the session')

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

    main_account_pk = request.POST['main_account']
    secondary_account_pk = request.POST['secondary_account']
    personal_account_pk = request.POST.get('personal_account')
    amount = request.POST['amount']

    entry = {'ma': main_account_pk, 'sa': secondary_account_pk, 'pa': personal_account_pk, 'a': amount}
    request.session['entries'].append(entry)
    request.session.modified = True

    ma = MainAccount.objects.get(pk=main_account_pk)
    sa = SecondaryAccount.objects.get(pk=secondary_account_pk)
    pa = PersonalAccount.objects.get(pk=personal_account_pk)

    entry_json = {'ma': ma.name, 'sa': sa.name, 'pa': pa.name, 'a': amount}

    session_entries = entry_json

    return JsonResponse(session_entries, safe=False)

def discard_session_entry(request):
    del request.session['entries'][-1]
    request.session.modified = "True"

    return HttpResponse('')
