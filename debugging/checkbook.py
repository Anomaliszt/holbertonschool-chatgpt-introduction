#!/usr/bin/env python3

class Checkbook:
    """
    A simple Checkbook class to manage deposits, withdrawals, and check the balance.

    Attributes:
    self.balance (float): The current balance in the checkbook.

    Methods:
    deposit(amount): Adds the specified amount to the balance.
    withdraw(amount): Deducts the specified amount from the balance if sufficient funds exist.
    get_balance(): Prints the current balance.
    """

    def __init__(self):
        """
        Initializes the Checkbook with a starting balance of 0.0.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Deposits the specified amount into the checkbook.

        Parameters:
        amount (float): The amount to deposit into the checkbook.

        Returns:
        None
        """
        self.balance += amount
        print(f"Deposited ${amount:.2f}.")
        print(f"Current Balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        """
        Withdraws the specified amount from the checkbook if sufficient funds exist.

        Parameters:
        amount (float): The amount to withdraw from the checkbook.

        Returns:
        None
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}.")
            print(f"Current Balance: ${self.balance:.2f}")

    def get_balance(self):
        """
        Prints the current balance in the checkbook.

        Parameters:
        None

        Returns:
        None
        """
        print(f"Current Balance: ${self.balance:.2f}")

def main():
    """
    Main function to interact with the Checkbook class.
    Allows the user to deposit, withdraw, check balance, or exit the program.

    Parameters:
    None

    Returns:
    None
    """
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ").lower()
        if action == 'exit':
            break
        elif action == 'deposit':
            try:
                amount = float(input("Enter the amount to deposit: $"))
                cb.deposit(amount)
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        elif action == 'withdraw':
            try:
                amount = float(input("Enter the amount to withdraw: $"))
                cb.withdraw(amount)
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        elif action == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
