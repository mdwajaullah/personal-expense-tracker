# Personal Expense Tracker & Monthly Report Generator

## About the Project
Personal Expense Tracker is a Python-based command-line project that helps users record and manage their daily expenses.

It allows users to add expenses, categorize transactions, calculate total spending, and generate monthly expense reports.

This project demonstrates the use of Python built-in modules, user-defined modules, and external packages.

## Features
- Record personal expenses.
- Add expense descriptions.
- Categorize expenses.
- Enter expense amounts and dates.
- Generate unique transaction reference IDs.
- Validate expense amounts.
- Calculate total spending.
- Calculate category-wise expenses.
- Generate monthly expense reports.
- Display expenses in a formatted table.

## Expense Categories
- Food
- Travel
- Study
- Bills
- Other

## Technologies Used
- Python
- Command Line Interface (CLI)
- Tabulate Package

## Python Modules Used
- datetime – Manage transaction dates and monthly reports.
- random – Generate transaction reference IDs.
- math – Perform rounding and calculations.
- os – Handle file paths and existence checks.

## Python Concepts Used
- User-defined Modules
- import Statement
- from import
- Import Aliases
- Built-in Modules
- External Packages
- pip Installation
- Functions
- Lists and Dictionaries
- Date and Time Handling

## Project Structure

```text
expense_tracker/
│
├── main.py
├── expense_utils.py
├── report_utils.py
└── requirements.txt
```

## Installation

Install the required external package:

```bash
python -m pip install tabulate
```

Or install dependencies using:

```bash
pip install -r requirements.txt
```

## Requirements

Add the following package to requirements.txt:

```text
tabulate
```

## How to Run the Project

1. Install Python on your computer.
2. Install the required package.
3. Download or clone this repository.
4. Open the project folder in VS Code.
5. Run the following command:

```bash
python main.py
```

## Example Output

```text
Expense Tracker

Enter description: Metro card recharge
Enter category: Travel
Enter amount: 500
Enter date (YYYY-MM-DD, blank for today):

Reference ID: EXP-482731

----- MONTHLY EXPENSE REPORT -----

Date        Description          Category    Amount
2026-10-27  Metro card recharge  Travel      500.00

Total spending: 500.00
Travel total: 500.00
Report month: October 2026
```

## Project Purpose
The main purpose of this project is to understand Python modules, packages, and libraries and learn how to organize a Python program into separate reusable files.

## Author
Md Wajaullah

## Project Level
Intermediate – Python Modules, Packages & Libraries