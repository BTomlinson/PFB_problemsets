#! /usr/bin/env  python
import sys

#simply making a list of animals
animals = ['horse', 'cow', 'moose', 'hound','mouse']

#using print to print out the middle element 'moose'
print(animals[2])

#replace moose with dog and print the list
animals.remove('moose')
animals.insert(2,'dog')
print(animals)

#add a new element 'bird' to the end
animals.append('bird')

#add a new element 'zebra' to the beginning
animals.insert(0,'zebra')

#add another element at index position 4
animals.insert(4,'kangaroo')

#remove and element from the end, bye bye birdie!
animals.pop()

#remove the first element of the list, bye mr zebra
animals.remove(animals[0])

#remove the dog
animals.remove('dog')

#join animals list with a new list of animals, animals2
animals2 = ['monkey', 'giraffe','wallaby']
animals.extend(animals2)





