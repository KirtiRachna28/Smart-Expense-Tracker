# main.py
from tracker.expense import Expense
from tracker.storage import save_expense, load_expenses
from tracker.analytics import total_expense, expense_by_category
from tracker.utils import print_expenses, format_currency

def main():
    print("Welcome to Smart Expense Tracker!\n")
    
    while True:
        print("\n1. Add Expense")
        print("2. View All Expenses")
        print("3. View Summary")
        print("4. Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            date = input("Enter date (YYYY-MM-DD): ")
            category = input("Enter category: ")
            amount = input("Enter amount: ")
            description = input("Enter description (optional): ")
            expense = Expense(date, category, amount, description)
            save_expense(expense)
            print("Expense saved successfully!")
        
        elif choice == "2":
            expenses = load_expenses()
            print_expenses(expenses)
        
        elif choice == "3":
            expenses = load_expenses()
            print(f"\nTotal Expense: {format_currency(total_expense(expenses))}")
            print("\nExpense by Category:")
            for cat, amt in expense_by_category(expenses).items():
                print(f"  {cat}: {format_currency(amt)}")
        
        elif choice == "4":
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
