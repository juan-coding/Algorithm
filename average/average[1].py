# An average just combines the counting and sum patterns and divides when the 
# the loop is done

count = 0 
sum = 0
print ('Before',count, sum)
for value in [9,41,12,3,74,15]:
	count = count +1
	sum = sum + value 
	print (count,sum, value)
	
print ('Average',sum/count)


'''
count =0 
sum1 = 0
value = input("please enter vector of data:")
for i in value:
	count = count +1
	sum1 = sum1+i
	print(count,sum1,i)
'''