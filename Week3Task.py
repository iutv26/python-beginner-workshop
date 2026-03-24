class BudgetTracker:
    def __init__(self):
        self.balance = 0.0
    def add_income(self, amount):
        """Method to add income to the balance."""
        if amount > 0:
            self.balance += amount
            print(f"Successfully added income: ${amount:.2f}")
        else:
            print("Error: Income amount must be greater than 0.")

    def add_expense(self, amount):
        """Method to deduct an expense from the balance."""
        if amount > 0:
            self.balance -= amount
            print(f"Successfully added expense: ${amount:.2f}")
        else:
            print("Error: Expense amount must be greater than 0.")
    def show_balance(self):
        """Method to display the current balance."""
        print(f"Current Balance: ${self.balance:.2f}")


def main():
    tracker = BudgetTracker()
    print("Welcome to the Budget Tracker!")
    while True:
        print("\n--- Main Menu ---")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Show Balance")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            try:
                amount = float(input("Enter income amount: $"))
                tracker.add_income(amount)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif choice == '2':
            try:
                amount = float(input("Enter expense amount: $"))
                tracker.add_expense(amount)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif choice == '3':
            tracker.show_balance()
        elif choice == '4':
            print("Exiting Budget Tracker. Have a great day!")
            break  

        else:
            print("Invalid choice. Please select a number from 1 to 4.")
if __name__ == "__main__":
    main()