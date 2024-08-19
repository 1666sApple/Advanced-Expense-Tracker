from django import forms
from django.forms import ModelForm
from .models import Expense

class ExpenseForm(ModelForm):
    class Meta:
        model = Expense
        fields = ('name', 'amount', 'price', 'category')  
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Enter expense name',
                }),
            'amount': forms.NumberInput(attrs={
                'placeholder': 'Enter amount',
                }),
            'price': forms.NumberInput(attrs={
                'placeholder': 'Enter price',
                }),
            'category': forms.TextInput(attrs={
                'placeholder': 'Enter category',
                }),
        }
