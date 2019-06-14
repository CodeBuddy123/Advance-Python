#showing memory improvement of generators over list

from random import choice
import time
names=['Raj','Ash','Raghu']
subjects=['Oracle','Python','Java','SQL']

def people_list(num):
	results=[]
	for i in range(num):
		person={'id':i,'name':choice(names),'subject':choice(subjects)}
		results.append(person)
	return results


def people_generator(num):
	for i in range(num):
		person={'id':i,'name':choice(names),'subject':choice(subjects)}
		yield person
t1=time.perf_counter()
#people=people_list(2000) 0.006614799999999997
people_generator(2000)    #3.599999999999437e-06 time taken in this is less(10^-6)
t2=time.perf_counter()

print('Total time taken:',t2-t1)
