from django import forms
from models import Transaction


class TransactionForm(forms.ModelForm):

    class Meta:
        model = Transaction
        fields = ('receiver_accno', 'amount', 'transaction_password')
