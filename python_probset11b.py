#! /usr/bin/env python3

#this now expands on the previously created class by adding new methods with defined functions for our class

class DNAsequence(object):
	def __init__(self, genename, sequence,	organism):
		self.genename = genename
		self.sequence = sequence
		self.organism = organism
	def pullgenename(self):
		print('this gene is named',self.genename)
	def getorganisminfo(self):
		print('the',self.genename,'gene is from',self.organism)
	def getlengthinfo(self):
		gene = self.genename
		geneseq = self.sequence
		length = len(self.sequence)
		print('the sequence of', gene,'is', geneseq,'and it is',length,'nt long')
	def nucleotidecomposition(self):
		geneseq = self.sequence
		length = len(self.sequence)
		Gs = geneseq.count('G')
		Cs = geneseq.count('C')
		GCcont = ((Gs+Cs)/length)
		print('The GC content of', self.genename, 'is', GCcont)
#now lets test the methods of the class, give it the following info first:
query = DNAsequence('SSR42','ATTGTGATGATCCCGAT','s. aureus')

#test the pullgenename method
query.pullgenename()

#test the getorganisminfo method
query.getorganisminfo()

#test the getlengthinfo method
query.getlengthinfo()

#test the nucelotidecomposition method
query.nucleotidecomposition()
