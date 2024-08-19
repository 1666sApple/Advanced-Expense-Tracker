from django.db import models

# Create your models here.
class Expense(models.Model):
    name = models.CharField(max_length=100)
    amount = models.PositiveIntegerField() 
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    category = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    
    def __str__(self):
        return f"{self.name} - {self.category} - {self.amount} @ {self.price}"