word = "python"
d = dict()
for c in word:
	if c in d:
		d[c]=d[c]+1
	else:
		d[c]=1
print(d)
