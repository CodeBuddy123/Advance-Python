#In hybrid inheritance to resolve method resolution order MRO algorithm is used
#Python provides, inbuilt mro() method to be called on any Class

class A:
	pass

class B(A):
	pass

class C(A):
	pass

class D(B,C):
	pass

print(A.mro())
print(B.mro())
print(C.mro())
print(D.mro())

'''
output:-
[<class '__main__.A'>, <class 'object'>]
[<class '__main__.B'>, <class '__main__.A'>, <class 'object'>]
[<class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
[<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]

'''