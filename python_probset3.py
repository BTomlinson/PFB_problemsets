#! /usr/bin/env  python3
import sys

#defining variables
#retrieve variables from the command line
dna = sys.argv[1]

#print dna sequence in uppercase
DNA=dna.upper()

#find and print length of dna
print('length of sequence:',len(DNA))

#print number of As
print('number of As:',DNA.count('A'))

#print number of Ts
print('number of Ts:',DNA.count('T'))

#print number of As below length
print('number of Gs:',DNA.count('G'))

#print number of As below length
print('number of Cs:',DNA.count('C'))

#translate DNA into RNA
print("RNA sequence:5'",DNA.replace('T','U'),"3'")

#save the RNA sequence as variable RNA
RNA=DNA.replace('T','U')

#count the Gs in the first 5 nucleotides of DNA
DNAfirst5 = DNA[0:5]
print('number of Gs in first 5 nts:',DNAfirst5.count('G'))

#print the reverse complement of DNA
RevDNA=DNA[::-1]
RevDNAsub1=RevDNA.replace('A','t')
RevDNAsub2=RevDNAsub1.replace('T','a')
RevDNAsub3=RevDNAsub2.replace('G','c')
RevCompDNA=RevDNAsub3.replace('C','g')
print("reverse complement '5",RevCompDNA.upper(),"3'")

#searching for EcoRI restriction site and spitting out location
print('EcoRI restriction site?:','GAATTC' in DNA)


