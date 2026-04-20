# Q.1

# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

# class Teacher(Person):
#     def __init__(self, name, age,subject):
#         super().__init__(name,age)
#         self.subject=subject
    
#     def teach(self):
#         print(f'{self.name} teacher who is {self.age} years old  teaches us {self.subject}')
              
# taklu_teacher=Teacher('rame',27,'science')
# taklu_teacher.teach()



# Q.2

# class Shape:
#     def __init__(self,color):
#         self.color=color
    
# class Circle(Shape):
#     def __init__(self,color,radius):
#         super().__init__(color)
#         self.radius=radius
#     def area(self):
#         print(f'the area of circle whose color is {self.color} and area is {self.radius*self.radius*3.14}')
# chota_circle=Circle('black',2)
# chota_circle.area()


# Q.3

# class Vehicle:
#     def __init__(self,brand,year):
#         self.brand=brand
#         self.year=year
    
# class Truck(Vehicle):
#     def __init__(self, brand, year,payload_capacity):
#         super().__init__(brand, year)
#         self.payload_capacity=payload_capacity

#     def load(self):
#         print(f'the {self.brand} truck has a total of payload capacity of {self.payload_capacity}')
# semi_truck=Truck('BMW',2016,'12ton')
# semi_truck.load()