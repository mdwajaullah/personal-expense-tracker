import expense_utils as eu
from expense_utils import total_spending, category_total, monthly_expenses
from tabulate import tabulate


def generate_monthly_report():
    if not monthly_expenses:
        print("No expenses recorded for this month.")
        return

    print("\nMonthly Expense Report:")
    print("-----------------------")
    table_data = []
    for ref_id, expense in monthly_expenses.items():
        table_data.append([
            ref_id,
            expense['description'],
            expense['category'],
            f"₹{expense['amount']}",
            expense['date']
        ])
    print(tabulate(table_data, headers=["Ref ID", "Description", "Category", "Amount", "Date"], tablefmt="grid"))   
    print("-----------------------")



    

def save_expenses_to_file(filename="monthly_expenses.txt"):
    with open(filename, "w") as file:
        for ref_id, expense in monthly_expenses.items():
            file.write(f"Ref ID: {ref_id}\n")
            file.write(f"Description: {expense['description']}\n")
            file.write(f"Category: {expense['category']}\n")
            file.write(f"Amount: ₹{expense['amount']}\n")
            file.write(f"Date: {expense['date']}\n")
            file.write("-----------------------\n")

    print(f"Expenses saved to {filename}.")

def monthly_summary():
    total = total_spending(monthly_expenses)
    print(f"\nTotal Spending for the Month: ₹{total}")

    categories = set(expense['category'] for expense in monthly_expenses.values())
    print("\nCategory-wise Spending:")
    for category in categories:
        category_total_amount = category_total(monthly_expenses, category)
        print(f"{category}: ₹{category_total_amount}")

