from django.shortcuts import render, redirect
from .forms import DataEntryForm
from accounts.models import (MainAccount, SecondaryAccount,
        PersonalAccount)
from django.http import JsonResponse, HttpResponse
from .models import EntryBundle, Entry
# Create your views here.

def data_entry(request):
    template = 'data_entry/data_entry.html'

    request.session['entries'] = [] #create or overwrite if already exists
    request.session['entries_counter'] = 1

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

def drcr_balance_check(entries):
    dr = 0
    cr = 0
    for entry in entries:
        if entry['e_type'] == 'dr':
            dr += int(entry['a'])
        elif entry['e_type'] == 'cr':
            cr += int(entry['a'])

    if dr == cr:
        return (1, dr, cr, dr-cr)
    elif dr>cr or cr>dr:
        return (-1, dr, cr, dr-cr)

def get_entry(request):

    main_account_pk = request.POST['main_account']
    secondary_account_pk = request.POST['secondary_account']
    personal_account_pk = request.POST.get('personal_account')
    amount = request.POST['amount']
    entry_type = request.POST['entry_type']
    entry_count = request.session['entries_counter']
    symbol_number = request.POST['symbol_number']

    entry = {'entry_count': entry_count, 'ma': main_account_pk, 'sa': secondary_account_pk, 'pa': personal_account_pk, 'a': amount, 'sn':symbol_number, 'e_type': entry_type}
    request.session['entries'].append(entry)
    request.session['entries_counter'] = request.session['entries_counter'] + 1
    request.session.modified = True

    ma = MainAccount.objects.get(pk=main_account_pk)
    sa = SecondaryAccount.objects.get(pk=secondary_account_pk)
    pa = PersonalAccount.objects.get(pk=personal_account_pk)
    drcr_balance_val = drcr_balance_check(request.session['entries'])

    entry_json = {'entry_count': entry_count, 'ma': ma.name, 'sa': sa.name, 'pa': pa.name, 'a': amount,  'sn': symbol_number, 'e_type': entry_type, 'drcr_balance_val': drcr_balance_val}

    session_entry = entry_json

    return JsonResponse(session_entry, safe=False)

def save_session_entries(request):

    if request.session['entries']:
        drcr_balance_check_val = drcr_balance_check(request.session['entries'])
        if drcr_balance_check_val[0] == 1:
            detail = request.POST['detail']
            entrybundle = EntryBundle(detail=detail)
            entrybundle.save()
            counter = 0
            for entry in request.session['entries']:
                ma_pk = entry['ma']
                sa_pk = entry['sa']
                pa_pk = entry['pa']

                ma = MainAccount.objects.get(pk=ma_pk)
                sa = SecondaryAccount.objects.get(pk=sa_pk)
                pa = PersonalAccount.objects.get(pk=pa_pk)
                sn = entry['sn']
                a = entry['a']
                e_type = entry['e_type']
                counter += 1

                entry = Entry(main_account=ma, secondary_account=sa, personal_account=pa, amount=a, entry_type=e_type, symbol_number=sn, entry_bundle=entrybundle, count=counter)
                entry.save()

            del request.session['entries']
            del request.session['entries_counter']
            return HttpResponse('reload')
        elif drcr_balance_check_val[0] == -1:
            return HttpResponse(status=400)

    return HttpResponse('')

def discard_session_entry(request):
    entry_count = int(request.GET['entry_count'])

    for index in range(len(request.session['entries'])):
        if request.session['entries'][index]['entry_count'] == entry_count:
            del request.session['entries'][index]
            request.session.modified = True
            print("entry deleted with entry count of:" + str(entry_count))
            break

    drcr_balance_val = drcr_balance_check(request.session['entries'])

    return JsonResponse(drcr_balance_val, safe=False)

def cancel_session_entries(request):
    if request.session['entries']:
        del request.session['entries']
        del request.session['entries_counter']

        return redirect('data_entry:data_entry')
    else:
        return HttpResponse('Something went wrong', status=400)
