#!/usr/bin/env python3
import sys
import re

#open the stupid fasta file
fastafile = open('Python_08.fasta','r')

#make your variables 

seqheader=''
fastadict={}

#go through each line and remove end whitespace
for line in fastafile:
	line = line.rstrip()
#if it starts with '>' and is a header, then assign it to seqheader. put seq header in the dictionary with an empty value assigned.
	if line.startswith('>'):
		seqheader = line
		fastadict[seqheader] = ''
#if it isnt a header, aka no '>', then assign it to the value for the last header key. add it on though (+=) dont overwrite.
	else:
		sequence = line
		fastadict[seqheader] += line

#make sure you print the dictionary, not something else!

print(fastadict)

#now lets see if we can count the ATGCs for each sequence.


for seqheader in fastadict:
#print the key
	print(seqheader)
#print the value of that key
	print(fastadict[seqheader])
#pull out unique nucleotides by making the value a set, cheater way since sets only keep unique values
	unique=set(fastadict[seqheader])
#print out the unique, should only have ATGC at most because none of our sequences have Ns
	print('unique nts:',unique)
#assign sequence to be the value of the key we have been discussing
	sequence = fastadict[seqheader]
#make an empty dictionary to store the counts
	ntcount={}
#make a loop
	for nt in sequence:
#if the nt has been accounted for...
		if nt in ntcount:
#then add +1 to the count for that nucleotide
			ntcount[nt] +=1
#if the nucleotide is already in the dictionary, no need to add the key, just add +1 to the value of the aalready existing key
		else:
			ntcount[nt] = 1
	print(ntcount)
