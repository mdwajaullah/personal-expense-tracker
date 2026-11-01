# Personal Expense Tracker & Monthly Report Generator

import random
from expense_utils import add_expense
from report_utils import generate_monthly_report, monthly_summary, save_expenses_to_file
print("\nExpense Tracker")

while True:
    print("\n1. Add Expense")
    print("2. Generate Monthly Report")
    print("3. Save Expenses to File")
    print("4. Monthly Summary")
    print("5. Exit")

    choice = input("\nEnter your choice (1-5): ")

    if choice == '1':
        add_expense()
    elif choice == '2':
        generate_monthly_report()
    
    elif choice == '3':
        save_expenses_to_file()
    
    elif choice == '4':
        monthly_summary()
    elif choice == '5':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")    

if __name__ == "__main__":
    print("Welcome to the Personal Expense Tracker & Monthly Report Generator!")