#! /usr/bin/env python3
import sys
import re


try:
	fileinput = sys.argv[1]
	print('User provided file:',fileinput)
	if not fileinput.endswith('.fasta'):
		raise ValueError
except ValueError:
	print('file must be a fasta file')
except IndexError:
	print('cannot locate file')
except: 
	print('Please provide a file name')

	


