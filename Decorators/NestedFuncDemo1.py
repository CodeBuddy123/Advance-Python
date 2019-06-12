#declaring a function inside a function is called nested function

def outer():
	print('outer func execution')
	def inner():
		print('inner func execution')
	print('Outer func calls inner')
	inner() #it is available only inside outer function

outer()

#inner()-->NameEror:'inner' not defined
          #inner is not available outside outer