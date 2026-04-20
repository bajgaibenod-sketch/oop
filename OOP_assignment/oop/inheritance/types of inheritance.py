
# Q.1

class Vehicle:
     def color(self):
          print('do u know what color i am ')
class Car(Vehicle):
     def color(self):
          base=super().color()
          print('blue ho color')
class ElectricCar(Vehicle):
     def color(self):
          base=super().color()
          print("i don't know")
vehicle_1=ElectricCar()
vehicle_1.color()
