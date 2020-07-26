from django import forms
from .models import Entry, SecondaryAccount

class DataEntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ('main_account', 'secondary_account',
                'personal_account', 'amount', 'entry_type',
                'symbol_number')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['secondary_account'].queryset = SecondaryAccount.objects.none()
        self.fields['amount'].widget.attrs['min'] = 0.01

        if 'main_account' in self.data:
            try:
                main_account_id = int(self.data.get('main_account'))
                self.fields['secondary_account'].queryset = SecondaryAccount.objects.filter(main_account_id=main_account_id).order_by('code')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty SecondaryAccount queryset
        elif self.instance.pk:
            self.fields['secondary_account'].queryset = self.instance.main_account.secondary_account_set.order_by('code')
