#! /usr/bin/env python3

#creating a class called DNAsequence
class DNAsequence(object):
	#define class attributes
	def __init__(self, genename, sequence,	organism):
		self.genename = genename
		self.sequence = sequence
		self.organism = organism
	#define a method for this class
	def getinfo(self):
		gene = self.genename
		length = len(self.sequence)
		print('the',gene,'is',length,'nt long')

#now if i want to use this class, give it the info needed and run the getinfo function:
DNAsequence('SSR42','ATTGTGATGATCCCGAT','s. aureus').getinfo()

#thats pretty ugly though so its nicer to define the input for the class as a variable first. then run whatever function you want.

geneofinterest = DNAsequence('SSR42','ATTGTGATGATCCCGAT','s. aureus')
geneofinterest.getinfo()

