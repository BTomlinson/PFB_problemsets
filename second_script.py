#! /usr/bin/env python3
import sys

#defining variables
#DNA="TATTGTGATCTGTGAGACACCCGTGACGAGAGTC"

#defines guess as first argument and converts it to an integer

guess = sys.argv[1]
guess = int(guess)

#tell the user what their guess was

print("your guess was",guess)

#to learn more about how large of a number A is

if guess > 16:
	print("too high")
elif guess < 16:
	print("too low")
else:
	print("you win, but you should probably get out more")


 



