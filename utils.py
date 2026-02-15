# tracker/utils.py

def format_currency(amount):
    return f"${amount:.2f}"

def print_expenses(expenses):
    if not expenses:
        print("No expenses recorded.")
        return
    print(f"{'Date':10} | {'Category':10} | {'Amount':10} | Description")
    print("-" * 50)
    for exp in expenses:
        print(f"{exp.date:10} | {exp.category:10} | {format_currency(exp.amount):10} | {exp.description}")
