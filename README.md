
FairShare – Group Expense Tracker

Project Description:

FairShare is a Django-based web application designed to help groups fairly manage and split shared expenses. The project simplifies group expense management by allowing users to input various expenses made by different individuals during shared activities like trips, dinners, or events. The system calculates how much each participant owes to ensure the total expenses are equally distributed among the group members.

Core Features:

Expense Entry: Add expense details including the payer's name, amount spent, and description of the expense.
Automatic Equal Split Calculation: The app calculates how much each person owes to equalize the group's total spending.
Expense History: View the last 5 expense entries for better tracking.
Delete Expense Entry: Remove incorrect or unnecessary entries.
Database Integration: Store all expense data in the database using Django ORM.
Export to PDF: Generate and download a PDF file summarizing the expense report.
User-Friendly Interface: Styled using Bootstrap for a clean and responsive layout.

Example Use Case:

Rahul spends ₹100, Ravi spends ₹50, and Suraj spends nothing.
Total spending = ₹150. Each person should pay ₹50.
Since Rahul paid ₹100 and Ravi ₹50, Suraj owes ₹50 to Rahul.
The app calculates such settlements automatically.

Technologies Used:

Backend: Python, Django Framework
Frontend: Bootstrap 5 (for design and responsiveness)
Database: SQLite (default Django database)
PDF Generation: ReportLab library

Key Functionalities (Step-wise):

Add Expense: Users can enter expenses directly via the input form.
Calculate Settlements: The system calculates the amount each person owes after an expense entry.
Expense History: View the last 5 expense records.
Delete Entry: Option to delete any incorrect entry.
Export to PDF: Generate a PDF summary of the expense report and download it.

Project Goals:

Ensure fairness in group expense distribution.
Provide a simple and effective way to manage shared expenses.
Easy data export and deletion options for better financial tracking.
