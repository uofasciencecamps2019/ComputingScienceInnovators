# Python Advanced Assignments

### Task
**Create 2 Python programs: A bank account program, and a combination lock program**

For the bank account program, make a bank account class with a deposit, withdraw, and display function (all are included in the template file in this repository)

For the combination lock program, make a combination lock class with a reset, left turn, right turn, and is_open function (all are included in the template file in this repository)

### Rules
1. Asking your peers for help is okay, but try not to copy and paste their code
2. If you get any code from peers or online sources, cite your sources
3. Make sure your code is compatible with Python3 (some things you look up will work for Python2 but not Python3)

**General rule of thumb:** If you can explain your code in your own words, that proves that you can understand it


### Code formatting
Examples has been provided to you in this repository ([bank.py](https://github.com/UofAScienceCamps2018/Python/blob/master/advanced/bank.py), [lock.py](https://github.com/UofAScienceCamps2018/Python/blob/master/advanced/lock.py))

```python
#!/usr/bin/env python3

"""
File: bank.py
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
```

```python
#!/usr/bin/env python3

"""
File: lock.py
Name:

Description
Concepts covered: Classes, assertion
"""


class ComboLock:
    def __init__(self, key1, key2, key3):
        self.key1 = key1
        self.key2 = key2
        self.key3 = key3
        
        self.dial = 0
        self.attempt = []  # the current 3-number combo being entered into the lock
        self.lefts = 0

    # Sets the dial at zero
    def reset(self):
        # Code here

    # Turns the dial a number of ticks counter-clockwise and updates attempt
    def turn_left(self, ticks):
        # Code here

    # Turns the dial a number of ticks clockwise and updates attempt list
    def turn_right(self, ticks):
        # Code here

    # Returns true if the lock is open (attempt == keys), false otherwise
    def isopen(self):
        # Code here

    # String representation of the ComboLock class
    def __repr__(self):
        return 'ComboLock({}, {}, {})'.format(self.key1, self.key2, self.key3)


# WARNING: Don't touch this function, it is to be left as it is
def test1():
    lock = ComboLock(25, 10, 0)
    assert str(lock) == 'ComboLock(25, 10, 0)' # __repr__ 
    assert not lock.isopen()
    
    # lock should open - basic
    lock.reset()
    lock.turn_right(25)
    lock.turn_left(15)
    lock.turn_right(50)
    assert lock.isopen()
       
    # lock should open - basic with reset in the middle
    lock.reset()
    lock.turn_right(35)
    lock.turn_left(5)
    lock.reset()
    lock.turn_right(25)
    lock.turn_left(15)
    lock.turn_right(50)
    assert lock.isopen()

    # lock should open - advanced 
    # the user turns the dial more than one full rotation
    lock.reset()
    lock.turn_right(85)
    lock.turn_left(135)
    lock.turn_right(50)
    assert lock.isopen()   
    
    # lock should not open - wrong combination
    lock.reset()
    lock.turn_right(15)
    lock.turn_left(25)
    lock.turn_right(10)
    lock.turn_left(24)    
    assert not lock.isopen()
 
    
# WARNING: Don't touch this function, it is to be left as it is
def test2():    
    lock = ComboLock(40, 30, 5)
    assert str(lock) == 'ComboLock(40, 30, 5)' 
    assert not lock.isopen()
    
    # lock should open 
    lock.reset()
    lock.turn_right(40)
    lock.turn_left(10)
    lock.turn_right(35)
    assert lock.isopen()
    
    # lock should not open - wrong combination
    lock.reset()
    lock.turn_left(20)
    lock.turn_left(10)
    lock.turn_left(25)    
    assert not lock.isopen()
    
 
def test():
    test1()
    test2()
    print("Passed all test cases")
    
if __name__ == "__main__":
    test()
```
