#! /usr/bin/env python3

# import modules
import argparse

# define our function
def get_args():
	# create an ArgumentParser object ('parser') that will hold all the information necessary to
	# parse the command line
	parser = argparse.ArgumentParser(description = "This script returs the Fibonacci number at a specified position in the Fibonacci sequence")
	
	# define positional arguments
	parser.add_argument("num", help = "The Fibonacci number you wish to calculate", type = int)
	
	# define optional arguments
	parser.add_argument("-v", "--verbose", help = "Print verbose output", action = 'store_true')
	
	# parse the arguments
	return parser.parse_args()

# function to calculate the Fibonacci sequence	
def fib(n):
	# do the calculation
	a,b = 0,1
	for i in range (args.num):
		a,b = b, a+b
	# return the value
	return a 
	
def main():
	if args.verbose: 
		print("The Fibonacci number for", args.num, "is", fib(args.num))
	else:
		print(fib(args.num))
		
args = get_args()	
	
main()

#./fibpy 3 -v

#+ just print, - calculate the reverse complement, return, and print