#!/usr/bin/env python3

#open the new sequence file and print it 
opSeq = open('Python_06.seq.txt', 'r')
print(opSeq.read())

#the Python_06.seq.txt contains reverse complements in the format seqName\tsequence\n

#to save the above sequences to a file in unix easily, can just run this .py script and redirect to a new file. aka go back to unix and write: ./python_probset6b.py > newfilename.seq.txt

count = 0
with open('Python_06.seq.txt', 'r') as sequences:
	for line in sequences:
		count+=1
print('Number of lines:',count)





