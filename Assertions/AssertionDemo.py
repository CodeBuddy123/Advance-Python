#Assertions are used for debbuging purpose
#By default, assertions are enabled in python
#To run py file by disabling assertions on client machine,run using py -O file_name.py

def square_it(x):
	return x*x


assert square_it(2)==4,"The Square of 2 is 4"
assert square_it(3)==9,"The Square of 3 is 9"
assert square_it(5)==25,"The Square of 5 is 25"

print(square_it(2))
print(square_it(4))
print(square_it(5))