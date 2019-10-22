#!/usr/bin/env python3
import sys
import re

fileinput=sys.argv[1]
blastresults = open(fileinput,'r')
print(type(blastresults))


for line in blastresults:
	line = line.rstrip()
	if line.startswith('#'):
		continue
	qseqid, sseqid, percid, alen, mismat, gaps, q_start, q_end, s_start, s_end, evalue, bits = line.split('\t')
	print(alen,percid,evalue)

