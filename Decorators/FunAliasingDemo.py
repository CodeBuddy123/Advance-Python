#Giving another name to function is called as function aliasing

def wish(name):
	print('Hello Good Morning!',name)

greeting=wish            #greeting is new name to the function
print(id(wish))
print(id(greeting))

wish('Ramesh') 
greeting('Kumar')