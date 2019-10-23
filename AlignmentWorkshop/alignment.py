#!/usr/bin/env python3

#purpose of this script is to parse a fasta file of contigs, sort longest to shortest length. Get the total number of contigs/2 for the halfway point and spit this number out. Then the total length of the first half of contigs.

#read in all the contigs. sort longest to shortest. find total length of ALL contigs and divide by 2. see how many contigs it takes to get you to that length. can do an if <#size keep going through the loop type function.

fastafile = open('ecoli_0.25.contigs.fasta','r')

fastacontigs = {}
ID = ''

for line in fastafile:
	line = line.rstrip()
	if line.startswith('>'):
		ID = line
		fastacontigs[ID]=''
	else:
		fastacontigs[ID]+= line

#print(fastacontigs)
#passed check, have a dictionary of ID : contigsequence now.

#make a list of contigs anda list of each contig length

contiglength = []
contiglist = []


for key in fastacontigs:
	contiglist.append(fastacontigs[key])
	contiglength.append(len(fastacontigs[key]))
	
#print(contiglist)
#print(contiglength)
#passed check, have a list of the sequence for each contig now and another list listing each contig length

#ok so N50 is half the length of the sum of the contigs. Lets combine all the contigs (which we now have a list of) into one massive string, caluclate the length, and divide by 2

allcontigscomb = ''

for contig in contiglist:
	allcontigscomb += str(contig)
print(len(allcontigscomb)/2)	

#awesome this worked. Now we need to figure out how many of our longest contigs we need to reach ND50. So first, order the contig lengths so theyre largest to smallest.

contiglength.sort(
