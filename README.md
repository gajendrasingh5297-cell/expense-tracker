# Expense Tracker (Python CLI)

Project for **Python Essentials - Evaluated Course Project**.

A simple command-line application to record and analyse daily expenses. Data is saved in a JSON file, so nothing is lost when the program closes.

## Features
- Add an expense (amount, category, note, auto date)
- View all expenses in a table with total
- Delete an expense by ID
- Category-wise summary with percentages
- Filter expenses by category
- Input validation and error handling

## Concepts Used
Variables and data types, lists, dictionaries, loops, conditionals, functions, string formatting, file handling (JSON), exception handling, the `datetime` module.

## Requirements
- Python 3.8 or higher
- No external libraries needed

## How to Run
```bash
python expense_tracker.py
```

## Menu
```
1. Add expense
2. View all expenses
3. Delete expense
4. Category summary
5. Filter by category
6. Exit
```

## Sample Output
```
ID  Date        Category     Amount  Note
-------------------------------------------------------
1   2026-09-30  Food         120.00  Lunch
2   2026-09-30  Travel        50.00  Bus fare
-------------------------------------------------------
Total: Rs 170.00
```

## Project Structure
```
expense_tracker.py   # main program
expenses.json        # auto-created data file
README.md
```

## Author
Your Name Here
