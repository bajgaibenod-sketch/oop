# Q.1

class Employee:
    company='TechCorp'
    def __init__(self,name,role):
        self.name=name
        self.role=role
employee_1=Employee('rajesh','MD')
employee_2=Employee('ramesh','CEO')
employee_3=Employee('john','staff')
print(f'{employee_1.name} works for {Employee.company} and is a {employee_1.role}')
print(f'{employee_2.name} works for {Employee.company} and is a {employee_2.role}')
print(f'{employee_3.name} works for {Employee.company} and is a {employee_3.role}')


# Q.2
class Employee:
    count=0
    def __init__(self):
        Employee.count+=1
employee_1=Employee()
employee_2=Employee()
employee_3=Employee()
employee_4=Employee()
employee_5=Employee()
print(Employee.count)


# Q.3


class Dog:
    species = "Canine"

    def __init__(self,breed):
        self.species=breed

d1 = Dog('pitbull')
d2=Dog('bulldog')
print(d1.species)       
print(d2.species)        
print(Dog.species)       