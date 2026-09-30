"""
Expense Tracker - Python Essentials Evaluated Course Project
A command-line app to record, view, delete and summarise daily expenses.
Data is stored in a JSON file so it persists between runs.
"""

import json
import os
from datetime import date

DATA_FILE = "expenses.json"
CATEGORIES = ["Food", "Travel", "Shopping", "Bills", "Education", "Other"]


def load_expenses():
    """Load expenses from the JSON file. Return empty list if none exists."""
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        print("Warning: could not read data file. Starting fresh.")
        return []


def save_expenses(expenses):
    """Write the list of expenses to the JSON file."""
    with open(DATA_FILE, "w") as f:
        json.dump(expenses, f, indent=4)


def choose_category():
    """Ask the user to pick a category and return its name."""
    print("\nCategories:")
    for i, cat in enumerate(CATEGORIES, start=1):
        print(f"  {i}. {cat}")
    while True:
        try:
            choice = int(input("Choose category number: "))
            if 1 <= choice <= len(CATEGORIES):
                return CATEGORIES[choice - 1]
            print("Please enter a number from the list.")
        except ValueError:
            print("Invalid input. Enter a number.")


def add_expense(expenses):
    """Add a new expense."""
    while True:
        try:
            amount = float(input("Amount (Rs): "))
            if amount <= 0:
                print("Amount must be greater than 0.")
                continue
            break
        except ValueError:
            print("Invalid amount. Try again.")

    category = choose_category()
    note = input("Note (optional): ").strip()
    expense = {
        "id": max((e["id"] for e in expenses), default=0) + 1,
        "date": str(date.today()),
        "amount": amount,
        "category": category,
        "note": note,
    }
    expenses.append(expense)
    save_expenses(expenses)
    print("Expense added successfully!")


def view_expenses(expenses):
    """Display all expenses in a table."""
    if not expenses:
        print("\nNo expenses recorded yet.")
        return
    print(f"\n{'ID':<4}{'Date':<12}{'Category':<11}{'Amount':>9}  Note")
    print("-" * 55)
    for e in expenses:
        print(f"{e['id']:<4}{e['date']:<12}{e['category']:<11}{e['amount']:>9.2f}  {e['note']}")
    print("-" * 55)
    print(f"Total: Rs {sum(e['amount'] for e in expenses):.2f}")


def delete_expense(expenses):
    """Delete an expense by its ID."""
    view_expenses(expenses)
    if not expenses:
        return
    try:
        target = int(input("\nEnter ID to delete: "))
    except ValueError:
        print("Invalid ID.")
        return
    for e in expenses:
        if e["id"] == target:
            expenses.remove(e)
            save_expenses(expenses)
            print("Expense deleted.")
            return
    print("ID not found.")


def category_summary(expenses):
    """Show total spending per category."""
    if not expenses:
        print("\nNo data to summarise.")
        return
    totals = {}
    for e in expenses:
        totals[e["category"]] = totals.get(e["category"], 0) + e["amount"]
    grand_total = sum(totals.values())
    print("\nSpending by category:")
    for cat, amt in sorted(totals.items(), key=lambda x: x[1], reverse=True):
        percent = amt / grand_total * 100
        print(f"  {cat:<10} Rs {amt:>9.2f}  ({percent:.1f}%)")


def search_by_category(expenses):
    """Show expenses of one chosen category."""
    category = choose_category()
    matches = [e for e in expenses if e["category"] == category]
    if not matches:
        print(f"No expenses found in {category}.")
        return
    view_expenses(matches)


def main():
    expenses = load_expenses()
    actions = {
        "1": ("Add expense", add_expense),
        "2": ("View all expenses", view_expenses),
        "3": ("Delete expense", delete_expense),
        "4": ("Category summary", category_summary),
        "5": ("Filter by category", search_by_category),
    }
    while True:
        print("\n===== EXPENSE TRACKER =====")
        for key, (label, _) in actions.items():
            print(f"{key}. {label}")
        print("6. Exit")
        choice = input("Select an option: ").strip()
        if choice == "6":
            print("Goodbye!")
            break
        if choice in actions:
            actions[choice][1](expenses)
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
