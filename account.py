        
class Account:
    def __init__(self, number, pin, owner):
        self.number = number
        self.__pin = pin
        self.__balance = 0
        self.owner = owner
        self.__transactions = []
        self.__overdraft_limit = 0
        self.__is_frozen = False
        self.__min_balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.__transactions.append(f"Deposit: {amount}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0:
            if self.__balance >= amount:
                self.__balance -= amount
                self.__transactions.append(f"Withdrawal: {amount}")
            else:
                if self.__overdraft_limit > 0 and self.__balance - amount + self.__overdraft_limit >= 0:
                    self.__balance -= amount
                    self.__transactions.append(f"Withdrawal: {amount} (overdraft)")
                else:
                    print("Insufficient funds.")
        else:
            print("Invalid withdrawal amount.")

    def view_account_details(self):
        print(f"Account Number: {self.number}")
        print(f"Account Owner: {self.owner}")
        print(f"Current Balance: {self.__balance}")

    def change_account_owner(self, new_owner):
        self.owner = new_owner

    def account_statement(self):
        for transaction in self.__transactions:
            print(transaction)

    def set_overdraft_limit(self, limit):
        self.__overdraft_limit = limit

    def interest_calculation(self, rate):
        if self.__balance > 0:
            interest = self.__balance * rate
            self.__balance += interest
            self.__transactions.append(f"Interest: {interest}")
        else:
            print("No balance to apply interest.")

    def freeze_account(self):
        self.__is_frozen = True

    def unfreeze_account(self):
        self.__is_frozen = False

    def transaction_history(self):
        for transaction in self.__transactions:
            print(transaction)

    def set_min_balance(self, balance):
        self.__min_balance = balance

    def transfer_funds(self, other_account, amount):
        if amount > 0:
            if self.__balance >= amount:
                self.withdraw(amount)
                other_account.deposit(amount)
                self.__transactions.append(f"Transfer: {amount} to {other_account.number}")
            else:
                if self.__overdraft_limit > 0 and self.__balance - amount + self.__overdraft_limit >= 0:
                    self.withdraw(amount)
                    other_account.deposit(amount)
                    self.__transactions.append(f"Transfer: {amount} to {other_account.number} (overdraft)")
                else:
                    print("Insufficient funds.")
        else:
            print("Invalid transfer amount.")

    def close_account(self):
        self.__transactions = []
        self.__balance = 0
        self.__overdraft_limit = 0
        self.__is_frozen = False
      

#example usage

my_account = Account("3432189", 1234, "Joy Cheshari")


my_account.deposit(1000)

my_account.withdraw(500)

my_account.view_account_details()

my_account.change_account_owner("Pearl Temko")

my_account.account_statement()

my_account.set_overdraft_limit(200)

my_account.interest_calculation(0.05)

my_account.freeze_account()

my_account.unfreeze_account()

my_account.transaction_history()

my_account.set_min_balance(100)

another_account = Account("987654321", 4321, "Faith Chebet")
my_account.transfer_funds(another_account, 200)


my_account.close_account()