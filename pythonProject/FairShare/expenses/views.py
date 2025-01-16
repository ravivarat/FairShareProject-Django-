from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import Expense
from .forms import ExpenseForm
from django.db.models import Sum
from reportlab.pdfgen import canvas


def home(request):
    expenses = Expense.objects.all().order_by('-date_added')
    form = ExpenseForm()
    recent_expenses = expenses[:5]

    # Collect unique payer names and calculate total spending
    payers = expenses.values_list('payer', flat=True).distinct()
    total_spent = expenses.aggregate(Sum('amount'))['amount__sum'] or 0
    num_people = len(payers)
    share_per_person = total_spent / num_people if num_people > 0 else 0

    # Calculate balances
    balances = {payer: (expenses.filter(payer=payer).aggregate(Sum('amount'))['amount__sum'] or 0) - share_per_person
                for payer in payers}

    # Calculate settlements
    def calculate_settlements(balances):
        creditors = [(payer, balance) for payer, balance in balances.items() if balance > 0]
        debtors = [(payer, -balance) for payer, balance in balances.items() if balance < 0]
        settlements = []

        while creditors and debtors:
            creditor, credit = creditors.pop()
            debtor, debt = debtors.pop()
            amount = min(credit, debt)

            settlements.append(f"{debtor} needs to pay ₹{amount:.2f} to {creditor}")

            credit -= amount
            debt -= amount

            if credit > 0:
                creditors.append((creditor, credit))
            if debt > 0:
                debtors.append((debtor, debt))

        return settlements

    settlements = calculate_settlements(balances)

    # Handle new expense submission
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, 'home.html', {
        'form': form,
        'expenses': expenses,
        'recent_expenses': recent_expenses,
        'total_spent': total_spent,
        'share_per_person': share_per_person,
        'balances': balances,
        'settlements': settlements
    })

def delete_expense(request, expense_id):
    expense = get_object_or_404(Expense, id=expense_id)
    expense.delete()
    return redirect('home')


def export_to_pdf(request):
    # Prepare PDF response
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="expense_report.pdf"'

    # Create a PDF canvas
    p = canvas.Canvas(response)
    p.setFont("Helvetica", 10)

    # Title of the PDF
    p.drawString(100, 800, "Expense Report - FairShare")
    p.drawString(100, 780, "------------------------------")

    # Add headers for the columns
    p.drawString(100, 760, "Payer | Amount | Description | Date Added")

    # Fetch all expenses from the database
    expenses = Expense.objects.all().order_by('-date_added')

    # Starting position to print entries
    y_position = 740  # Starting from a bit lower to leave space for headers

    # Loop through the expenses and write them to the PDF
    for expense in expenses:
        # Print each expense with details: payer, amount, description, date added
        expense_details = f"{expense.payer} | ₹{expense.amount} | {expense.description} | {expense.date_added.strftime('%Y-%m-%d %H:%M:%S')}"

        p.drawString(100, y_position, expense_details)

        y_position -= 20  # Move down for the next line

        # If we reach near the bottom of the page, create a new page
        if y_position < 100:
            p.showPage()  # End current page and start a new one
            p.setFont("Helvetica", 10)  # Reset the font after a new page
            p.drawString(100, 800, "Expense Report - FairShare")  # Title on new page
            p.drawString(100, 780, "------------------------------")  # Underline
            p.drawString(100, 760, "Payer | Amount | Description | Date Added")  # Headers
            y_position = 740  # Reset the y-position for the new page

    p.showPage()  # Ensure we close the page at the end
    p.save()  # Finalize and save the PDF

    return response  # Return the PDF as the response