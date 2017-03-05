import os
os.getcwd()
help(os.chdir)
os.chdir('/Users/Amy/Dropbox/12. Learning Python/2.py4e-master_Charles/code3') 

fname = input("Enter the file name: ")
try: 
	fhandle = open(fname)
except:
	print("file cannot be opened:", fname)
	exit()

counts = dict()
for lines in fhandle:
	word_list = lines.split()
	for word in word_list:
		counts[word]=counts.get(word,0)+1
print(counts)



