from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Temporary storage
expenses = []

# Expense Model
class ExpenseModel(BaseModel):
    name: str
    amount: float
    description: str | None = None


@app.get("/")
def root():
    return {"message": "Hello World!!!"}


# Get all expenses
@app.get("/expenses")
def get_expenses():
    return expenses


# Get expense by index (ID)
@app.get("/expenses/{expense_id}")
def get_expense_by_id(expense_id: int):
    if expense_id < 0 or expense_id >= len(expenses):
        return {"error": "Expense not found"}

    return expenses[expense_id]


# Create a new expense
@app.post("/create_expense")
def create_expense(expense: ExpenseModel):
    expenses.append(expense)

    return {
        "message": "Expense created successfully!",
        "expense": expense
    }