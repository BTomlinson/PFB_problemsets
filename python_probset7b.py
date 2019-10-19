#!/usr/bin/env python3

#download specialized re functions

import re

#open, read, and print the Python07 fasta file

#fastofile =open("Python_07.fasta","r")
#print(fastofile.read())
#fastofile.close()

#what type is fastofile?

#print(type(fastofile))

#yuck its an IO, lets make it a string
fastofile = open('Python_07.fasta','r')
fastofile_string=str(fastofile.read())
print(type(fastofile_string))

#ok cool so now we can work with fastofile_string. lets print out the sequence starters
found = re.search(r'>\S',fastofile_string)
print(found)

#it was able to find something so thats good. now lets find them all.
found2 = re.findall(r'>\S',fastofile_string)
print(found2)

#how many are there?
print('there are',len(found2))

#ok lets get the full sequence header using typical pattern and pattern group

findheaders = re.findall(r'>\S+',fastofile_string)
findwithgroup = re.findall(r'(>\S+)',fastofile_string)

print('sequence headers:',findheaders)
