#!/usr/bin/python3

class Checkbook:
    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        print("Current Balance: ${:.2f}".format(self.balance))

def get_valid_amount(action):
    while True:
        try:
            amount = float(input(f"Enter the amount to {action}: $"))
            if amount < 0:
                print("Amount must be positive. Please try again.")
            else:
                return amount
        except ValueError:
            print("invalid input. Please enter a valid number.")

def main():
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ")
        if action == 'exit':
            print("Exiting the program.")
            break
        elif action == 'deposit':
            amount = get_valid_amount("deposit")
            cb.deposit(amount)
        elif action == 'withdraw':
            amount = get_valid_amount("withdraw")
            cb.withdraw(amount)
        elif action == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
