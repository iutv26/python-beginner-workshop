#Updated person class with a greet method
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello, my name is", self.name, "and I am", self.age, "years old.")
        
person1 = Person("Alice", 25)
person2 = Person("Bob", 30)
person1.greet()
person2.greet()
print("\n")
#BankAccount System
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print("Withdrawn:", amount)

    def show_balance(self):
        print("Current balance:", self.balance)
account1 = BankAccount("Alice", 1000)
account1.show_balance()
account1.deposit(500)
account1.withdraw(300)
account1.withdraw(1500)
account1.show_balance()