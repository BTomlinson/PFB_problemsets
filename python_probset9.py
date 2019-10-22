#! /usr/bin/env python3
import sys
import re


#open the file the user supplies

fastafile = open(sys.argv[1])

fastadict = {}
ID = ''
sequence = ''

for line in fastafile:
  line = line.rstrip()
  if line.startswith('>'):
    ID = line
    fastadict[ID]=''
  else:
    fastadict[ID] += line

#check it made a dict
#print(fastadict)
#pass

#lets pull out all the 3 letter codons in each value
#extract the values from the fastadict
listofsequences = list(fastadict.values())
#check it worked
#print(listofsequences)
#print(type(listofsequences))
#yep passed, list of all values

#now pull out the codons for each sequence using regular expressions re
codons=[]
for dna in listofsequences:
	codons.append(re.findall(r'(.{3})',dna)) #finds the first 3, next 3... adds to list
print(codons)


#how about the next reading frame just for fun?
#codonsframe2=[]
#for dna in listofsequences:
	#dna2=dna[1:]
	#codonsframe2.append(re.findall(r'(.{3})',dna2))
#print(codonsframe2)
#the above code works but silenced to keep working with first reading frame


#instead of saving codons as list of a list from first reading frame, need to change code so it saves them with just a space between them
codons=[]
for dna in listofsequences:
  codons.append(re.findall(r'(.{3})',dna)) #finds the first 3, next 3... adds to list
codonsgrouped=[]
for dna2 in codons:
	print(' '.join(dna2))

