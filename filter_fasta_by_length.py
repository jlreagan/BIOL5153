#! /usr/bin/env python3

#do chapter 5&6
#assignment due Wednesday (chapters 5,6) and Friday (assignment #6)

#load the required modules


import argparse
from Bio import SeqIO

#create an ArgumentParser object ('parser') that will hold all the information necessary
parser = argparse.ArgumentParser(description="This script filters out sequences from a FASTA file that are shorter than user-specified length cutoff")


# use the add_argument() menthod to add a positional argument
# positional arguments are *required* inputs, so their order/position matters
# argparse treats all options as strings unless told to do otherwise

parser.add_argument("fasta", help="name of FASTA file")

# add an optional argument, the length cutoff for our filter
parser.add_argument("gff", help="name of GFF file")

# parse the arguments
args = parser.parse_args()

print("We're gonna open this FASTA file:", args.fasta)
print("filter sequences less than", args,min_seq_length, "nt in length")

for genome in SeqIO.parse(arggs.fasta, "fasta"):
	with open(args.gff) as lines:
		for line in lines.readlines():
			(seqname, source, feature, start, end, score, strand, frame, attribute)=line.split("\t")
			gene = line.split()[10]
			print(">{}_{}".format(seqname, gene) + '\n' + (genome.seq[int(start):(end)+1]))



#(species_name, type, begin, end) = line,split('\t')
#change parseGFF so that two input files come from Argparse
#use argparse as FASTA file and GFF file



