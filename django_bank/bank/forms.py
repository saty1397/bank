from django import forms
from models import Transaction


class TransactionForm(forms.ModelForm):

    class Meta:
        model = Transaction
        fields = ('receiver_accno.account_no','amount', 'transaction_password')
