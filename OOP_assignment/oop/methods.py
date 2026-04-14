
class Dog:
    name='buddy'
    breed='labrador'

    def noise(self,sound):
        self.sound=sound
        print(f'{self.name} is  making {self.sound} noise')
    def eat(self,eating):
        self.eating=eating
        print(f'{self.name} is eating {self.eating} while making {self.sound}')
dog1=Dog()
dog1.name='ram'
dog1.eat='chicken'
dog1.noise('bark1')
dog2=Dog()
dog2.name='wolf'
dog2.noise('bark2')
dog2.eat('milk')



# Q.1

class Greeter:
    pass
    def greet(self):
        print(f' hello my name is {self.name}!')
greeter_1=Greeter()
greeter_1.name='ram'
greeter_1.greet()


# Q.2

class Rectangle:
    width=12
    height=21
    def area(self):
        print(f'the area of rectangle having {self.width} width and {self.height} heigt is {self.height*self.width}')
area_a=Rectangle()
area_a.area()


# Q.3

class BankAccount:
    balance = 0

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. Balance: ${self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. Balance: ${self.balance}")
        else:
            print("Insufficient funds.")
    def check_balance(self,balance):
        print(f'your current balance is {self.balance} ')

acc = BankAccount()
acc.deposit(500) 
acc.check_balance(0)    # Deposited $500. Balance: $500
   # Deposited $500. Balance: $500
acc.withdraw(200)    # Withdrew $200. Balance: $300
acc.check_balance(0)    # Deposited $500. Balance: $500

acc.withdraw(400)    # Insufficient funds.
acc.check_balance(0) 

    
    
