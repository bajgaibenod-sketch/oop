# Q.1
# class Person:
#     def __init__(self,name,email,password):
#         self.name=name
#         self._email=email
#         self.__password=password
# person_1=Person('ramit','ramit@gmail.com','ramot123')
# print(person_1.name)
# print(person_1._email)  #woks but shouldn't be accesed directly
# print(person_1._Person__password) #works but we won't do this

    
# Q.2
# class SecretVault:
#     def __init__(self,code):
#         self.__code=code
    
# vault=SecretVault(1234)
# # print(vault.code)    #won't work
# print(vault._SecretVault__code)  #works fine



# Q.3

# class Person:
#     def __init__(self,name,email,password):
#         self.name=name
#         self._email=email
#         self.__password=password
#     def verify_password(self,guess):
#         if guess==self.__password:
#             return True
#         else:
#             return False
# guess=Person('binod','binod@gmail.com',12345)
# guess_1=guess.verify_password(6446)
# guess_2=guess.verify_password(12345)
# print(guess_1)
# print(guess_2)

        
