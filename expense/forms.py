from django import forms
from django.forms import ModelForm
from .models import Expense

class ExpenseForm(ModelForm):
    class Meta:
        model = Expense
        fields = ('name', 'amount', 'price', 'category')  # Added 'price' to fields
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Enter expense name',
                'class': 'border rounded-lg px-3 py-2 w-full'  # Added w-full for full width
            }),
            'amount': forms.NumberInput(attrs={
                'placeholder': 'Enter amount',
                'class': 'border rounded-lg px-2 py-2 w-full'  # Added w-full for full width
            }),
            'price': forms.NumberInput(attrs={  # Added widget for price
                'placeholder': 'Enter price',
                'class': 'border rounded-lg px-2 py-2 w-full'  # Added w-full for full width
            }),
            'category': forms.TextInput(attrs={
                'placeholder': 'Enter category',
                'class': 'border rounded-lg px-2 py-2 w-full'  # Added w-full for full width
            }),
        }
