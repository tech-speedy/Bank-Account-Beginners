class BankAccount:
    def __init__(self, account_name, balance=0.0):
        self.account_name = account_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"${amount} has been deposited. New balance: ${self.balance}")
        else:
            print("Deposit amount must be greater than zero.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"${amount} has been withdrawn. New balance: ${self.balance}")
        else:
            print("Insufficient balance or invalid amount.")

    def check_balance(self):
        print(f"Current balance: ${self.balance}")


def main():
    print("Welcome to the Bank Program!")
    account_name = input("Enter account holder's name: ")
    
    # Create a new bank account for the user
    account = BankAccount(account_name)

    while True:
        print("\nChoose an option:")
        print("1. Deposit money")
        print("2. Withdraw money")
        print("3. Check balance")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)

        elif choice == "2":
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)

        elif choice == "3":
            account.check_balance()

        elif choice == "4":
            print("Thank you for using the Bank Program!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
