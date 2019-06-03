#___str__ can be used to convert object to meaningful string representation but not otherway around
#repr can be used to convert object to string representation and string rep to object

import datetime
today=datetime.datetime.now() #creating today(datetime) object 
s=repr(today)                #converting today(datetime) object to string 
print(s)                     #printing on console
d=eval(s)                    #converting string object to datetime object
print(d)                     #printing on console
print(type(d))               #printing the type of d object