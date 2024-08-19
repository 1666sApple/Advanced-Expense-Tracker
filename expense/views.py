from django.shortcuts import render, redirect
from .models import Expense
from .forms import ExpenseForm

def index(request):
    expenses = Expense.objects.all()
    if request.method == "POST":
        expense_form = ExpenseForm(request.POST)
        if expense_form.is_valid():
            expense_form.save()
    else:
        expense_form = ExpenseForm()
        
    
    return render(request, 'expense/index.html', 
        {'expense_form': expense_form,
            'expenses':expenses})

def edit(request, id):
    expense = Expense.objects.get(id=id)
    expense_form = ExpenseForm(instance=expense)
    if request.method == "POST":
        expense = Expense.objects.get(id=id)
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('index')
        
    return render(request, 
        'expense/edit.html', 
        {'expense_form':expense_form})
    
def delete(request, id):
    if request.method == 'POST':
        expense = Expense.objects.get(id=id)
        expense.delete()
    return redirect('index')