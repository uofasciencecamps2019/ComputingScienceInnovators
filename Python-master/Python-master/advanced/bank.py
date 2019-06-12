#!/usr/bin/env python3

"""
File:
Name:

Bank account simulation to learn how to use classes in Python
Concepts covered: Classes

Base:       deposit, withdraw, view account
Extension:  (1) chequing/savings (2) savings growth (3) transaction history
"""

__author__      = "Tem Tamre"
__copyright__   = "ttamre@ualberta.ca"


class BankAccount:
    def __init__(self, name, balance=5000):
        # Code here
    
    def deposit(self, amount):
        # Code here

    def withdraw(self, amount):
        # Code here
    
    def showAccount(self):
        print("Name:", self.name)
        print("Balance:", self.balance)


def test():
    alex  = BankAccount("Alex")
    bobby = BankAccount("Bobby", 3250)

    # Testing Alex
    assert alex.name == "Alex"
    assert alex.balance == 5000
    alex.deposit(500)
    alex.deposit(1500)
    alex.withdraw(250.25)
    assert alex.balance == 6750.75
    alex.showAccount()

    # Testing Bobby
    assert bobby.name == "Bobby"
    assert bobby.balance == 3250
    bobby.deposit(alex.balance)
    bobby.withdraw(500)
    bobby.withdraw(1250.50)
    assert bobby.balance == 4749.5
    bobby.showAccount()


if __name__ == "__main__":
    test()
    print("Program success!")