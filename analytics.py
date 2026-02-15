# tracker/analytics.py

def total_expense(expenses):
    return sum(expense.amount for expense in expenses)

def expense_by_category(expenses):
    summary = {}
    for expense in expenses:
        summary[expense.category] = summary.get(expense.category, 0) + expense.amount
    return summary
