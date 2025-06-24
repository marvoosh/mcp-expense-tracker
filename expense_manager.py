import csv

expenses = []


def add_expense(amount, category, description, date):
    expenses.append({
        "amount": amount,
        "category": category,
        "description": description
    })


def write_to_csv():
    with open("expenses.csv", "w") as file:
        writer = csv.writer(file)
        writer.writerow(["Amount", "Category", "Description", "date"])
        for expense in expenses:
            writer.writerow([expense["amount"], expense["category"], expense["description"]])




