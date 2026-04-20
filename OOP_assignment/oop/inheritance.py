# class Animal:
#     def __init__(self,name):
#         self.name=name
#     def sound(self):
#         print(f'{self.name} makes sound')
#     def eat(self):
#         print(f'{self.name} eats  food')
# class Dog(Animal):
#     def __init__(self, name,breed):
#         super().__init__(name)
#         self.breed=breed
#     def eat(self):
#         print(f'{self.name} {self.breed}  eats  meat')
    
# bd=Dog('max','lab')
# bd.sound
# bd.eat()
# # c=Cow()
# # c.sound()
        

# Q.1


# class Vehicle:
#     def __init__(self,brand):
#         self.brand=brand
#     def honk(self):
#         print(f'{self.brand}  honks ')
# class Car(Vehicle):
#     pass
# car_1=Car('mercedes')
# car_1.honk()


# Q.2


# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def verification(self):
#         print(f'the name of student is {self.name} and age is {self.age}')

# class Student(Person):
#     pass
# student_1=Student('ram',24)
# student_1.verification()



# Q.3

# class Phone:
#     def __init__(self):
#         pass
#     def call(self):
#         print(f'someone is calling')

# class SmartPhone(Phone):
#     pass
# smartphone=SmartPhone()
# smartphone.call()

