#Exception handling for division operation
try:
	num1=int(input('Enter the Numerator:')) #Risky code,prone to Exception
	num2=int(input('Enter the Denominator:'))
	print(num1/num2)
except ZeroDivisionError:
	print('Denominator cannot be zero.')  #Alternate or handling code
except ValueError:
	print('Enter only Integer values')
