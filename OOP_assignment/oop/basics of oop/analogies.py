# Q.1

class Restaurant:
    def __init__(self,name,cuisine,rating):
        self.name=name
        self.cuisine=cuisine
        self.rating=rating
    
    def serve_food(self):
        print(f'the {self.name} serves {self.cuisine} cuisine')

    def get_review(self):
        print(f'the {self.name} has a rating of {self.rating}')
restaurant_1=Restaurant('abc','french',4.5)
restaurant_2=Restaurant('xyz','nepali',5.0)
restaurant_1.serve_food()
restaurant_1.get_review()
restaurant_2.serve_food()
restaurant_2.get_review()


# Q.2

class Pet:
    def __init__(self,name,species,energy):
        self.name=name
        self.species=species
        self.energy=energy
    def sleep(self):
        print(f'the energy of {self.name} is going up,his energy is {self.energy}  as he is sleeping now ')
    def eat(self):
        print(f'the energy of {self.name} is going up,his energy is {self.energy} as he is eating now')
    def play(self):
        print(f'the energy of {self.name} is going down ,his energy is {self.energy} as he is playing now ')
dog=Pet('blake','bull dog','1000')
bird=Pet('appu','pert','437')
dog.sleep()
dog.eat()
dog.play()
bird.sleep()
bird.eat()
bird.play()


# Q.3

class Phone():
    def __init__(self,name,brand,Ram):
        self.name=name
        self.brand=brand
        self.Ram=Ram
    def camera(self):
        print(f'the name of the phone is {self.name} and it has {self.Ram}gb of  RAM which goes by the brand name  {self.name} famous for having a great camera')
    def battery(self):
        print(f'the {self.name} is a great phone for using for a long time as its battery capacity is too good')
phone_A=Phone('iphone','apple',16)
phone_B=Phone('Redmi AC','Redmi',14)
phone_A.camera()
phone_B.battery()