#else block executes only when there is no exception in try block
#else block can be used to execute any code after successful flow in try block
#else block can be taken only along with try-except but not without try or without except
#only one else block can be taken utmost(either 0 or 1) along with try block

try:
	print('try')        
	print(10/0)          #exception raised in try, so else block is not executed
except:
	print('except')
else:                    #else block is taken right after except block [try-except-else-finally]seq
	print('else')
finally:
	print('finally')