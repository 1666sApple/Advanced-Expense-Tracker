from django import forms
from django.forms import ModelForm
from .models import Expense

class ExpenseForm(ModelForm):
    class Meta:
        model = Expense
        fields = ('name', 'amount', 'category')
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Enter expense name',
                'class': 'border rounded-lg px-2 py-2'
            }),
            'amount': forms.NumberInput(attrs={
                'placeholder': 'Enter amount',
                'class': 'border rounded-lg px-2 py-2'
            }),
            'category': forms.TextInput(attrs={
                'placeholder': 'Enter category',
                'class': 'border rounded-lg px-2 py-2'
            }),
        }
