# class BankAccount:
#     __total_accounts = 0  # private class variable

#     def __init__(self, owner, balance=0):
#         self.__owner = owner
#         self.__balance = balance
#         self.__transactions = []
#         BankAccount.__total_accounts += 1

#     @property
#     def balance(self):
#         return self.__balance

#     @property
#     def owner(self):
#         return self.__owner

#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             self.__transactions.append(f"+${amount:.2f}")
#             return True
#         return False

#     def withdraw(self, amount):
#         if 0 < amount <= self.__balance:
#             self.__balance -= amount
#             self.__transactions.append(f"-${amount:.2f}")
#             return True
#         return False

#     def get_statement(self):
#         return self.__transactions.copy()
    

#     @classmethod
#     def get_total_accounts(cls):
#         return cls.__total_accounts
    

#     def transfer(self,amount,accountn):
#         if self.__withdraw