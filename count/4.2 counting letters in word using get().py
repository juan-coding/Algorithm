
# using get()
print ("\n using get() function to making a concise programming")
d1 = dict()
for c in word:
	d1[c]=d1.get(c,0)+1  # return 0 when letter appear first time
print(d1)