from mcp.server.fastmcp import FastMCP
import expense_manager

mcp = FastMCP("expense-tracker")

@mcp.tool()
def add_expense_to_csv(amount, category, description, date):
    # expense_manager.add_expense(amount, category, description, date)
    expense_manager.write_to_csv(amount, category, description, date)
    return "Expenses added to tracker successfully"


# TODO:
# Current issue is I keep re-writing the CSV file insted of just appending at teh end.

