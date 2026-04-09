# # Q.1 
# class Book:
#     title='loots of goons'
#     author='binod bajgai'
#     pages=298
# print(Book.title)
# print(Book.author)
# print(Book.pages)



# Q.2

# class Pet:
#     pass
# pet_1=Pet()
# pet_1.name='samir'
# pet_1.age=6
# print(pet_1.name)
# print(pet_1.age)
# pet_1.age=7
# print(pet_1.age)


# Q.3

class Product:
    pass
product__1=Product()
product__1.name='facewash'
product__1.price=499
product__1.quantity=1
total_cost_1=product__1.price*product__1.quantity
product__2=Product()
product__2.name='brush'
product__2.price=99
product__2.quantity=3
total_cost_2=product__2.price*product__2.quantity
total_spent=total_cost_2+total_cost_1
print(f'''your total is {total_spent}
you have spent Rs.{total_cost_2} on {product__2.name} amd Rs.{total_cost_2} on {product__1.name}''')

