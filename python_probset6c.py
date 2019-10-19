#!/usr/bin/env python3
import sys

fastafile = open('Python_08.fasta','r')

fastdick = {}
ID = ''
sequence = ''

for line in fastafile:
	line = line.rstrip()
	if line.startswith('>'):
		ID = line
		fastdick[ID]=''
	else:
		fastdick[ID] += line
#ok the above works. it is saying, for each line in fastafile, remove end whitespace.
#then, if the line starts with '>', set ID variable to line, then assign this ID key an empty value '' in the dictionary.
#if the line doesnt start with '>' then make that line the value of the ID key. += means itll keep adding on instead of overwriting.
#in other words, fastdick[ID]+=line translates to:
#		fastdick[ID]    				=					fastdick[ID]					+	line
# 	^ammend the value of key 					^the current value 		^tack on the new line value

print(fastdick)
