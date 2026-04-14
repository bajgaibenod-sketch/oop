class Temperature:
    def __init__(self,celsius):
        self.__celsius=celsius

    @property
    def celsius(self):
        return self.__celsius
    
    @celsius.setter
    def celsius(self,value):
        if value<-273.15:
            raise ValueError('invalid')
        self.__celsius=value 
temperature_1=Temperature(35)
print(temperature_1.celsius)
# temperature_1.celsius=-300
print(temperature_1.celsius)



# Q.2

class Employee:
    def __init__(self,employee_id,salary):
        self.__employee_id=employee_id
        self.__salary=salary
    
    @property
    def employee_id(self):
        return self.__employee_id
    @property
    def salary(self):
        return self.__salary
    @salary.setter
    def salary(self,amount):
        if amount<0:
            raise ValueError('amount must be positive')
            self.__salary=amount
employee=Employee(124,12000)
print(employee.salary)
employee.salary=-1231
print(employee.salary)

# Q.3
 
class Rectangle:
    def __init__(self,height,width):
        self.__height=height
        self.__width=width
    @property
    def height(self):
        return self.__height
    @property
    def width(self):
        return self.__width
    @height.setter
    def height(self,value):
        if value<0:
            raise ValueError('invalid Input')
        
        self.__height=value
    @width.setter
    def width(self,value1):
        if value1<0:
            raise ValueError('invalid input')
        
        self.__width=value1
    @property
    def area(self):
        return self.__height*self.__width
        
rectangle=Rectangle(2,3)
print(rectangle.area)
rectangle.width=-2
print(rectangle.width)
        
        





        