# Generated by Django 4.2.3 on 2023-08-07 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_expense_remaining_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='allocated_amount',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='expense',
            name='remaining_amount',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
