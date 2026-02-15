# tracker/__init__.py

# Import key modules so they are accessible from the package directly
from .expense import Expense
from .storage import save_expense, load_expenses
from .analytics import (
    total_expense,
    expense_by_category,
    monthly_expense,
    filter_expenses_by_category,
    filter_expenses_by_date_range
)
from .utils import print_expenses, format_currency

# Optional: define what is publicly available when importing *
__all__ = [
    "Expense",
    "save_expense",
    "load_expenses",
    "total_expense",
    "expense_by_category",
    "monthly_expense",
    "filter_expenses_by_category",
    "filter_expenses_by_date_range",
    "print_expenses",
    "format_currency"
]
