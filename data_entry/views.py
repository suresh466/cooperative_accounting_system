from django.shortcuts import render
from .forms import DataEntryForm
from accounts.models import SecondaryAccount

# Create your views here.

def data_entry(request):
    template = 'data_entry/data_entry.html'

    if request.method == 'POST':
        form = DataEntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            print(entry.main_account)
            print(entry.secondary_account)
            print(entry.personal_account)
            print(entry.amount)
    else:
        form = DataEntryForm

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
