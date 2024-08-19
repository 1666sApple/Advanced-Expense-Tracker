from django.shortcuts import render
from .models import Expense
from .forms import ExpenseForm

def index(request):
    if request.method == "POST":
        expense_form = ExpenseForm(request.POST)
        if expense_form.is_valid():
            expense_form.save()
    else:
        expense_form = ExpenseForm()
    
    return render(request, 'expense/index.html', {'expense_form': expense_form})
