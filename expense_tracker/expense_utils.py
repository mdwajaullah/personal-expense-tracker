from random import random
from datetime import date as dt
import math

monthly_expenses = {}
def add_expense():
    
    description = input("Enter description: ")
    category = input("Enter category: ")
    amount = int(input("Enter amount (₹): ")) 
    date = input("Enter date (YYYY-MM-DD, blank for today):")
    if not validate_amount(amount):
        return

    if not date:
        date = dt.today().strftime("%Y-%m-%d")
        ref_id = "EXP-" + str(random.randint(100000, 999999))
        
        monthly_expenses[ref_id] = {
            "description": description,
            "category": category,
            "amount": amount,
            "date": date
        }

def validate_amount(amount):
    try:
        if amount < 0:
            raise ValueError("Amount cannot be negative.")
    except ValueError as e:
        print(f"Invalid amount: {e}")
        return False

def total_spending(monthly_expenses):
    total = sum(expense["amount"] for expense in monthly_expenses.values())
    return total

def category_total(monthly_expenses, category):
    total = sum(expense["amount"] for expense in monthly_expenses.values() if expense["category"] == category)
    return total



