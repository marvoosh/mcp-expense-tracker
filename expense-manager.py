class ExpenseManager:
    def __init__(self):
        self.expenses = []

    def add_expense(self, amount, category, description):
        self.expenses.append({
            "amount": amount,
            "category": category,
            "description": description
        })


