import csv
import os

EXPENSES = []
EXPENSES_FILE = os.path.join(os.path.dirname(__file__), "expenses.csv")


# def add_expense(amount: int, category: str, description: str, date: str) -> str:
#     EXPENSES.append({
#         "amount": amount,
#         "category": category,
#         "description": description,
#         "date": date
#     })


def write_to_csv(amount, category, description, date):
    with open(EXPENSES_FILE, "w") as file:
        writer = csv.writer(file)
        writer.writerow([amount, category, description, date])




