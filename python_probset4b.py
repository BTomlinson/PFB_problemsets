#! /usr/bin/env  python3


#save a list of taxa
taxa = ['sapiens','erectus','neanderthalensis']

#checking what type taxa is:
print('Taxo is a', type(taxa))

#split taxa into individual words and print the results
taxa_it = iter(taxa)
for taxon in taxa_it:
	print(taxon)

#splitting taxa list based on commas, must convert into a string first
species = ', '.join(taxa)
print(species)
print(type(species))

#show me what the first element in the species string is
print(species[1])
#SURPRISE YOU CANT, ITS A STRING SO YOU JUST GET 'a' which is the [1] index position

#sort the taxon LIST alphabetically
print(sorted(taxa))

#sort taxa list by length of each string
print(sorted(taxa, key=len))

