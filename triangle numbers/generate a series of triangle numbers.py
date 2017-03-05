# Using a generator that generates a series of triangle numbers
def triangleNums():
	'''generate series of triangle numbers'''
	tn = 0
	counter = 1
	while (True):
		tn = tn + counter
		yield tn 
		counter = counter + 1 


g = triangleNums()
print(next(g)) # 1
print(next(g)) # 3
print(next(g)) # 6

