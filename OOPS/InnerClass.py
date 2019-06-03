class Outer:
	def __init__(self):
		print('Outer class object creation')

	class Inner:
		def __init__(self):
			print('Inner class object creation')

		def m1(self):
			print('from inner class m1 method')
'''
o=Outer()
i=o.Inner()
i.m1()
'''
Outer().Inner().m1()