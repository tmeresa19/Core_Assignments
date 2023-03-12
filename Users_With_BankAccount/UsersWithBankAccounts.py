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
        
#===========================Users with Bank Accounts===========================

# =======================use package to differenciate different classes instead of putting diffeent classes in the same file=============

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts = []

# 
    def add_account(self, balance=0, interest_rate=0.02):
        account = BankAccount(balance, interest_rate)
        self.accounts.append(account)
        return account

# 
    def make_deposit(self, account_index, amount):
        account = self.accounts[account_index]
        account.deposit(amount)

# 
    def make_withdrawal(self, account_index, amount):
        account = self.accounts[account_index]
        account.withdraw(amount)

# 
    def display_user_balance(self, account_index):
        account = self.accounts[account_index]
        account.display_account_info()

# 
user = User("John", "john@domain.com")
account1 = user.add_account(balance=1000)
account2 = user.add_account(balance=500)

# 
user.make_deposit(0, 200)
user.make_withdrawal(1, 100)
user.display_user_balance(0)
user.display_user_balance(1)
