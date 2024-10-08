# Generated by Django 5.1 on 2024-08-19 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("expense", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="expense",
            name="price",
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name="expense",
            name="amount",
            field=models.PositiveIntegerField(),
        ),
    ]
