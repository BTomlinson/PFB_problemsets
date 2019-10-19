#!/usr/bin/env python3

#download specialized re functions

import re

#test if 'nobody' is in Python_07_nobody.txt. first convert to a string because the document is actually a scary input file type. ew. then search the new string for 'Nobody'

namelist = open('Python_07_nobody.txt','r')
poem  = namelist.read()

if re.search(r'Nobody',poem):
	print('Nobody home!')

#ok so nobody is home. lets change nobody to Glen Coco

newpoem = re.sub('Nobody','Dormy Staniels', poem)
print(newpoem)


