#!/usr/bin/env python3
import sys

#dictionary of things
randomthings = {'animal':'cow', 'person':'obama', 'sport':'jailai'}
print(randomthings)

#print an empty line
print()

#print out the person named then say this is someone you miss.
print(randomthings['person'])
print('i miss',randomthings['person'])

#empty line
print()

#printing out fav animal but do so by referencing the key
fav_animal = 'animal'
print(randomthings[fav_animal])

#add to the dictionary a place
randomthings['place'] = 'bottom of river'
print(randomthings)

#empty line
print()
#print the place value only
print(randomthings['place'])

print()

#printing out place but when place is defines as variable wherewehidebodies
wherewehidebodies = 'place'

print('we hide the bodies at',randomthings[wherewehidebodies])

print()

#make the first user input define the value for a new key, house, in the dictionary.
randomthings['house']=sys.argv[1]
print(randomthings)

print()

#using FOR loop to print out the keys and values. randos means keys, [randos] means values assigned to the keys
for randos in randomthings:
	print(randos,randomthings[randos])

print()

#now do the same but after eachother
for randos in randomthings:
	print(randos)
	print(randomthings[randos])

print()

#now print all the keys, then print all the values
for randos in randomthings:
	print(randos)
for randos in randomthings:
	print(randomthings[randos])


