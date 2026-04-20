
# Q.1
# class Product:
#     def __init__(self,name,price):
#         self.name=name
#         self.price=price
# class Electronics(Product):
#     def __init__(self, name, price,warranty_years):
#         super().__init__(name, price)
#         self.warranty_years=warranty_years
#         print(f'{self.name} is Rs.{self.price} and has a warrranty of {self.warranty_years} years')
# samagri=Electronics('laptop',1050000,1)



# Q.2

# class Bird:
#     def describe(self):
#         print('does bird can talk')
# class Parrot(Bird):
#     def describe(self):
#         base=super().describe()
#         print('and i can talk')
# panchi=Parrot()
# panchi.describe()


# Q.3


# class Account:
#     def display(self):
#         print('and the ammount is 150 rupiya')
# class SavingAccount(Account):
#     def display(self):
#         base=super().display()
#         print('faack the interest is 20 percent')
# mero_khaata=SavingAccount()
# mero_khaata.display()