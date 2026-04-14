class Temperature:
    def __init__(self,celsius):
        self.celsius=celsius

    @property
    def value(self):
        return self.__celsius
    
    @value.setter
    def value(self,degree):
        if degree<=-273.15:
            self.__celsius=degree
p=Temperature(124)
print(p.celsius)
p.celsuis=455
print(p.celsius)

    