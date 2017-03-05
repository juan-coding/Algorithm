
# How would we change this to make it find the smallest value in the list?
print ('......find largest value.............')
laregest_so_far = -1
print ('Before',laregest_so_far)
for the_num in [9,41,12,3,74,15]:
	if the_num > laregest_so_far:
		laregest_so_far=the_num
	print (laregest_so_far,the_num)

print ('After',laregest_so_far)



print ('......find smallest value.............')

# Find smallest value
# Method 1: take an large aribtray number for our hypothesis number
smallest_so_far = 100 # arbitray 100 or 10000000....
print ('Before',laregest_so_far)
for the_num in [9,41,12,3,74,15]:
	if the_num < smallest_so_far:
		smallest_so_far=the_num
	print (smallest_so_far,the_num)

print ('After',smallest_so_far)


# Method 2: 

smallest_so_far = None # None is constant character
print ('Before',smallest_so_far)
for value in [9,41,12,3,74,15]:
	if smallest_so_far is None:
		smallest_so_far=value
	elif value< smallest_so_far:
		smallest_so_far=value
	print (smallest_so_far,value)

print ('After',smallest_so_far)


# or 
smallest_so_far = None # None is constant character
print ('Before',smallest_so_far)
for value in [9,41,12,3,74,15]:
	if smallest_so_far is None or value < smallest_so_far:
		smallest_so_far=value
		print (smallest_so_far,value)
print ('After',smallest_so_far)



