#Garbage collector is inside PVM, which is used to destroy useless objects

import gc
print(gc.isenabled()) #by default,it is enabled

gc.disable() #disabled

print(gc.isenabled())

gc.enable() #enable

print(gc.isenabled())