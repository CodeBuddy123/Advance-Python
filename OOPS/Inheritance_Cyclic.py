#python doesnt support cyclic inheritance

'''
class A(A):
	pass      error-'A' is not defined
'''

class A(B):
	pass        # error-'B' is not defined

class B(A):
	pass
