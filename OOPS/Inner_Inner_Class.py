class Outer:
	def __init__(self):
		print('Outer class object creation')

	class Inner:
		def __init__(self):
			print('Inner class object creation')

		class InnerInner:
			def __init__(self):
				print('inner inner object creation')
			def m1(self):
				print('m1 method of InnerInner class')
	
Outer().Inner().InnerInner().m1()
'''
o=Outer()
i=o.Inner()
inn=i.InnerInner()
inn.m1()
'''

