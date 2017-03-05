def counter(low,high):
	current = low
	while current <= high:
		yield current
		current = current+1

for c in counter(3,8):
	print(c)