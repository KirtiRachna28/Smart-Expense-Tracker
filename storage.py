# tracker/storage.py
import csv
from tracker.expense import Expense

CSV_FILE = "data/expenses.csv"

def save_expense(expense):
    """Append an expense to the CSV file"""
    with open(CSV_FILE, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["date", "category", "amount", "description"])
        # Write header if file is empty
        file.seek(0, 2)  # Go to end of file
        if file.tell() == 0:
            writer.writeheader()
        writer.writerow(expense.to_dict())

def load_expenses():
    """Load all expenses from the CSV file"""
    expenses = []
    try:
        with open(CSV_FILE, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                expense = Expense(
                    date=row['date'],
                    category=row['category'],
                    amount=row['amount'],
                    description=row['description']
                )
                expenses.append(expense)
    except FileNotFoundError:
        pass  # No file yet
    return expenses
