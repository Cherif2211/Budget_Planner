import os

BUDGET_DIR = "data/budgets"

class BudgetManager:
    def __init__(self, user):
        self.user = user
        self.budget_file = f"{BUDGET_DIR}/{self.user}.txt"
        self.budget = self.load_budget()

    def load_budget(self):
        if not os.path.exists(self.budget_file):
            return {"income": 0, "expenses": [], "goal": 0, "savings_percentage": 0, "savings": 0}
        
        budget = {"income": 0, "expenses": [], "goal": 0, "savings_percentage": 0, "savings": 0}
        with open(self.budget_file, "r") as file:
            for line in file:
                key, value = line.strip().split(":")
                if key == "income":
                    budget["income"] = float(value)
                elif key == "expenses":
                    budget["expenses"] = list(map(float, value.split(","))) if value else []
                elif key == "goal":
                    budget["goal"] = float(value)
                elif key == "savings_percentage":
                    budget["savings_percentage"] = float(value)
                elif key == "savings":
                    budget["savings"] = float(value)
        return budget

    def save_budget(self):
        if not os.path.exists(BUDGET_DIR):
            os.makedirs(BUDGET_DIR)
        with open(self.budget_file, "w") as file:
            file.write(f"income:{self.budget['income']}\n")
            file.write(f"expenses:{','.join(map(str, self.budget['expenses']))}\n")
            file.write(f"goal:{self.budget['goal']}\n")
            file.write(f"savings_percentage:{self.budget['savings_percentage']}\n")
            file.write(f"savings:{self.budget['savings']}\n")

    def view_budget(self):
        print(f"\nBudget for {self.user}:")
        print(f"Income: {self.budget['income']}")
        print(f"Expenses: {sum(self.budget['expenses'])}")
        print(f"Goal: {self.budget['goal']}")
        print(f"Savings Percentage: {self.budget['savings_percentage']}%")
        print(f"Saved Amount: {self.budget['savings']}")
        print(f"Remaining: {self.budget['income'] - sum(self.budget['expenses'])}")

    def add_income(self):
        try:
            amount = float(input("Enter income amount: "))
            self.budget["income"] += amount
            self.update_savings()
            self.save_budget()
            print("Income added successfully.")
        except ValueError:
            print("Invalid amount. Please try again.")

    def add_expense(self):
        try:
            amount = float(input("Enter expense amount: "))
            self.budget["expenses"].append(amount)
            self.save_budget()
            print("Expense added successfully.")
        except ValueError:
            print("Invalid amount. Please try again.")

    def set_goal(self):
        try:
            goal = float(input("Set your savings goal: "))
            self.budget["goal"] = goal
            self.save_budget()
            print("Goal set successfully.")
        except ValueError:
            print("Invalid amount. Please try again.")

    def set_savings_percentage(self):
        try:
            percentage = float(input("Enter the percentage of income to save (0-100): "))
            if 0 <= percentage <= 100:
                self.budget["savings_percentage"] = percentage
                self.update_savings()
                self.save_budget()
                print(f"Savings percentage set to {percentage}%.")
            else:
                print("Invalid percentage. Please enter a value between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    def update_savings(self):
        self.budget["savings"] = (self.budget["income"] * self.budget["savings_percentage"]) / 100
