#!/usr/bin/env python3

import sys

#import and open the BAM file

inputBAM = sys.argv[1]
BAMfile = open(inputBAM, 'r')

#make the BAM file into a dictionary

Bamdict = {}

for line in BAMfile:
	line.rstrip()
	listofBam = line.split('\t')
	gene = listofBam[2]
	read = listofBam[0]
#would be best to really pull the gene away from the trans by doing:
#	gene, trans = gene.split('^') 
#the gene and trans are written in the file as gene^trans but can just leave trans attached to it, totally fine 
	if gene not in Bamdict:
		Bamdict[gene] = set()
		Bamdict[gene].add(read)
	else:
		Bamdict[gene].add(read)
#print(Bamdict)
#passed

Readcountdict={}

for gene in Bamdict:
	Readcountdict[gene] = len(Bamdict[gene])
for gene in Readcountdict:
	print(gene,'\t',Readcountdict[gene])

#stuck here though because i need to sort by highest value 

for key,value in sorted(Readcountdict.items(), key=lambda item: item[1], reverse=True):
	print ('%s\t\t%s' % (key, value))



