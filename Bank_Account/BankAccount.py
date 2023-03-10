# ==================================Bank Account Class===================

class BankAccount:
    def __init__(self, balance=0, interest_rate=0.02):
        self.balance = balance
        self.interest_rate = interest_rate

    def deposit(self, amount):
        self.balance += amount
        print("Deposit is successful")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawal is successful")
        else:
            print("You don't have enough funds to withdraw")

    def display_account_info(self):
        print(f"Balance: {self.balance}")

    def yield_interest(self):
        interest_earned = self.balance * self.interest_rate
        self.balance += interest_earned
        print(
            f"Interest earned: {interest_earned}, New balance: {self.balance}")
