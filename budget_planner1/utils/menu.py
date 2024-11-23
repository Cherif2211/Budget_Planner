from budget.budget_manager import BudgetManager
from colorama import init, Fore

init()

def show_menu(user):
    manager = BudgetManager(user)
    while True:
        print(Fore.MAGENTA +"__________________________________________________________________")
        print(Fore.BLUE +"\n                    ---* Menu *---"+ Fore.RESET)
        print(Fore.MAGENTA +"1. View Budget")
        print("2. Add Income")
        print("3. Add Expense")
        print("4. Set Goal")
        print("5. Set Savings Percentage")
        print("6. Exit"+ Fore.RESET)

        choice = input(Fore.GREEN +"Choose an option: "+ Fore.RESET)

        print(Fore.CYAN +"")
        if choice == "1":
            manager.view_budget()
        elif choice == "2":
            manager.add_income()
        elif choice == "3":
            manager.add_expense()
        elif choice == "4":
            manager.set_goal()
        elif choice == "5":
            manager.set_savings_percentage()
        elif choice == "6":
            print(Fore.MAGENTA +"Goodbye see you next time ."+ Fore.RESET)
            break
        else:
            print(Fore.RED +"Invalid choice. Please try again."+ Fore.RESET)
