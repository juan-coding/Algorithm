laregest_so_far = -1
print ('Before',laregest_so_far)
for the_num in [9,41,12,3,74,15]:
	if the_num > laregest_so_far:
		laregest_so_far=the_num
	print (laregest_so_far,the_num)

print ('After',laregest_so_far)



# or set initial laregest_so_far as 'None' value
print ('....................')
laregest_so_far=None
print ('Before', laregest_so_far)
for value in [9,41,12,3,74,15]:
	if laregest_so_far is None:
		laregest_so_far=value
	elif value > laregest_so_far:
		laregest_so_far=value
	print (laregest_so_far,value)
print ('After',laregest_so_far)