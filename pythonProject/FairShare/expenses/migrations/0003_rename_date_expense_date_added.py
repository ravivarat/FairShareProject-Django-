# Generated by Django 5.1.4 on 2025-01-05 07:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0002_alter_expense_amount_alter_expense_description_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='expense',
            old_name='date',
            new_name='date_added',
        ),
    ]