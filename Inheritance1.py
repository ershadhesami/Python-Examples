# Author: Ahmad Ershad Hesami
# Author URI: https://www.facebook.com/ershad.hesami/
# Author Email: personal.aeh@outlook.com
# Date: 4/2/2020
# Description: A small python program
class Account:

    def __init__(self, name, balance = 0):
        self.name = name
        self.balance = balance
        print(f"Dear {self.name}!, Your account has been created successfully, you balance is ${self.balance} .")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"You have successfully deposited ${amount} to you account")
        else:
            print("Amount less than one can't be deposited")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"You have successfully withdrawn ${amount} from you account")
        else:
            print("You don't have enough balance")

    def checkBalance(self):
        print(f"Dear {self.name}!, You have ' ${self.balance} ' in your account")


class SavingAccount(Account):
    pass


class CurrentAccount(Account):
    pass


# Test the Code

ac1 = CurrentAccount("Jamal")
ac1.deposit(300)
ac1.checkBalance()
ac1.withdraw(100)
ac1.withdraw(30)
ac1.checkBalance()
ac1.withdraw(200)
ac1.withdraw(170)
ac1.checkBalance()
ac1.deposit(0)