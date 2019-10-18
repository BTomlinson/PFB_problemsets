#! /usr/bin/env python3

opPython = open('Python_06.txt', 'r')
newPython = open('NewPython.txt','w')

#simply open and read the contents of Python_06.txt

print(opPython.read())



print()


#uppercase everything line by line in Python_06.txt and print the result

opPython = open('Python_06.txt','r')
for line in opPython:
	line = line.upper()
	line = line.rstrip()
	print(line)

#for space
print()

#do the same but instead write the results to a new file Python_06.uc.txt

with open('Python_06.txt','r') as songread, open('Python_06_uc.txt','w') as songwrite:
	for line in songread:
		line = line.strip()
		capitalizedlines = line.upper()
		songwrite.write(str(capitalizedlines+'\n'))

newsong = open('Python_06_uc.txt','r')	
print(newsong.read())
