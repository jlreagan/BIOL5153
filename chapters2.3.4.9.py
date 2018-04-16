#####CHAPTER 2

#PRINT FUNCTION
#how quotation marks affect output
print ("Hello World!")
print ("She said, 'Hello world'")
print ('He said, "Hello world"')
#how to include a new line in the middle of a string
print("Hello/nworld")

#STORING STRINGS
my_dna = "ATGCGTA"
print(my_dna)
#change the value of my_dna
my_dna = "TGGTCCA"
banana = "ATGCGTA"

#CONCATENATION
my_dna = "AATT" + "GGCC"
print(my_dna)
#printed value= AATTGGCC
upstream = "AAA"
my_dna = upstream + "ATGC"
print ("Hello" + " " + "world")

#LENGTH OF A STRING
dna_length = len("AGTC")
print(dna_length)
my_dna = "ATGC"

#CAPITALIZATION VS. LOWERCASE
print(my_dna.lower())
print("ATGC")
len(my_dna)

#BEFORE/AFTER FUNCTION
my_dna = "ATGC"
print("before: " + my_dna)
lowercase_dna = my_dna.lower()
print("after: " + my_dna)

#REPLACING
protein = "vlspadktnv"
#replace valine with tyrosine
print(protein.replace("v", "y"))
print(protein.replace("vls", "ymt"))
print(protein)

#EXTRACTING A STRING
protein = "vlspadktnv"
#print positions three to five
print(protein[3:5])
#positions start at zero, not one
print (protein[0:6])
#go beyond the end is equivalent to stopping at the end
print (protein[0:60])

#COUNTING AND FINDING SUBSTRINGS
protein = "vlspadktnv"
first_residue = protein [0]
#count amino acide residues
valine_count = protein.count('v')
lsp_count = protein.count('lsp')
tryptophan_count = protein.count('w')
print("valines: " + str(valine_count))
print("lsp: " + str(lsp_count))
print("tryptophans: " + str(tryptophan_count))
protein = "vlspadktnv"
print(str(protein.find('p')))
print(str(protein.find('kt')))
print(str(protein.find('w')))

#CALCULATE AT CONTENT OF DNA SEQUENCE
my_dna = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
length = len(my_dna)
a_count = my_dna.count('A')
t_count = my_dna.count('T')
print("length: " + str(length))
print("A count: " + str(a_count))
print("T count: " + str(t_count))
at_content = (a_count + t_count) / length
print("AT content is" + str(at_content))

#COMPLEMENTING DNA
my_dna = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
replacement1 = my_dna.replace('A', 'H')
replacement2 = replacement1.replace('T', 'J')
replacement3 = replacement2.replace('C', 'K')
replacement4 = replacement3.replace('G', 'L')
replacement5 = replacement4.replace('H', 'T')
replacement6 = replacement5.replace('J', 'A')
replacement7 = replacement6.replace('K', 'G')
replacement8 = replacement7.replace('L', 'C')
print(replacement8)

my_dna = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
replacement1 = my_dna.replace('A', 't')
print(replacement1)
replacement2 = replacement1.replace('T', 'a')
print(replacement2)
replacement3 = replacement2.replace('C', 'g')
print(replacement3)
replacement4 = replacement3.replace('G', 'c')
print(replacement4)
print(replacement4.upper())

#RESTRICTION FRAGMENT LENGTHS
my_dna = "ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"
frag1_length = my_dna.find("GAATTC") + 1
frag2_length = len(my_dna) - frag1_length
print("length of fragment one is " + str(frag1_length))
print("length of fragment two is " + str(frag2_length))

#SPLICING OUT INTRONS
my_dna = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"
exon1 = my_dna[0:62]
exon2 = my_dna[90:10000]
print(exon1 + exon2)
coding_length = len(exon1 + exon2)
total_length = len(my_dna)
print(coding_length / total_length)
print(my_dna[0:62] + my_dna[62:90].lower() + my_dna[90:10000])














#####CHAPTER 3

#USING OPEN TO READ A FILE
my_file = open("dna.txt")
my_file_contents = my_file.read()
# remove the newline from the end of the file contents
my_dna = my_file_contents.rstrip("\n")
dna_length = len(my_dna)
print("sequence is " + my_dna + " and length is " + str(dna_length))

#OPEN FILE AND WRITE
my_file = open("dna.txt")
my_string = 'abcdefg'
print(my_string)
my_number = 42
print(my_number + 1)
my_file = open("dna.txt")
file_contents = my_file.read()
print(file_contents)

my_file = open("dna.txt")
my_file_contents = my_file.read()
# remove the newline from the end of the file contents
my_dna = my_file_contents.rstrip("\n")
dna_length = len(my_dna)
print("sequence is " + my_dna + " and length is " + str(dna_length))

my_file = open("out.txt", "w")
my_file.write("Hello world")

#CLOSING FILES
my_file = open("out.txt", "w")
my_file.write("Hello world")
# remember to close the file
my_file.close()

#my_file = open (r"c:\windows\home\jlreagan\pythonScripts\myfile.txt)

#SPLITTING GENOMIC DATA
my_dna = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"
exon1 = my_dna[0:62]
intron = my_dna[62:90]
exon2 = my_dna[90:10000]
print(exon1 + intron.lower() + exon2)

# open the file and read its contents
dna_file = open("genomic_dna.txt")
my_dna = dna_file.read()
# extract the different bits of DNA sequence
exon1 = my_dna[0:62]
intron = my_dna[62:90]
exon2 = my_dna[90:10000]
# open the two output files
coding_file = open("coding_dna.txt", "w")
noncoding_file = open("noncoding_dna.txt", "w")
# write the sequences to the output files
coding_file.write(exon1 + exon2)
noncoding_file.write(intron)

#WRITING A FASTA FILE
# set the values of all the header variables
header_1 = "ABC123"
header_2 = "DEF456"
header_3 = "HIJ789"
# set the values of all the sequence variables
seq_1 = "ATCGTACGATCGATCGATCGCTAGACGTATCG"
seq_2 = "actgatcgacgatcgatcgatcacgact"
seq_3 = "ACTGAC-ACTGT—ACTGTA----CATGTG"
print(header_1)
print(seq_1)
print(header_2)
print(seq_2)
print(header_3)
print(seq_3)
# make a new file to hold the output
output = open("sequences.fasta", "w")
# write the header and sequence for seq1
print('>' + header_1 + '\n' + seq_1)
print('>' + header_2 + '\n' + seq_2)
print('>' + header_3 + '\n' + seq_3)
# write the header and uppercase sequences for seq2
output.write('>' + header_2 + '\n' + seq_2.upper() + '\n')
print('>' + header_1 + '\n' + seq_1)
print('>' + header_2 + '\n' + seq_2.upper())
print('>' + header_3 + '\n' + seq_3.replace('-', ''))
# write the header and sequence for seq3 with hyphens removed
output.write('>' + header_3 + '\n' + seq_3.replace('-', '') + '\n')
#three files to hold output
output = open("sequences.fasta", "w")
output_1 = open(header_1 + ".fasta", "w")
output_2 = open(header_2 + ".fasta", "w")
output_3 = open(header_3 + ".fasta", "w")
output.write('>' + header_1 + '\n' + seq_1 + '\n')
output.write('>' + header_2 + '\n' + seq_2.upper() + '\n')
output.write('>' + header_3 + '\n' + seq_3.replace('-', '') + '\n')














#####CHAPTER 4 LISTS AND LOOPS
# set the values of all the sequence variables
seq_1 = "ATCGTACGATCGATCGATCGCTAGACGTATCG"
seq_2 = "actgatcgacgatcgatcgatcacgact"
seq_3 = "ACTGAC-ACTGT—ACTGTA----CATGTG"
# make three files to hold the output
output_1 = open(header_1 + ".fasta", "w")
output_2 = open(header_2 + ".fasta", "w")
output_3 = open(header_3 + ".fasta", "w")
#creating lists and retrieving elements
apes = ["Homo sapiens", "Pan troglodytes", "Gorilla gorilla"]
conserved_sites = [24, 56, 132]
print(apes[0])
first_site = conserved_sites[2]
apes = ["Homo sapiens", "Pan troglodytes", "Gorilla gorilla"]
chimp_index = apes.index("Pan troglodytes")
# chimp_index is now 1
#last element from the list
last_ape = apes[-1]
#lower ranks are class, order, and family
ranks = ["kingdom","phylum", "class", "order", "family"]
lower_ranks = ranks[2:5]
# lower ranks are class, order and family

apes = ["Homo sapiens", "Pan troglodytes", "Gorilla gorilla"]
apes.append("Pan paniscus")
print("There are " + str(len(apes)) + " apes")
apes.append("Pan paniscus")
print("Now there are " + str(len(apes)) + " apes")

apes = ["Homo sapiens", "Pan troglodytes", "Gorilla gorilla"]
monkeys = ["Papio ursinus", "Macaca mulatta"]
primates = apes + monkeys
print(str(len(apes)) + " apes")
print(str(len(monkeys)) + " monkeys")
print(str(len(primates)) + " primates")

ranks = ["kingdom","phylum", "class", "order", "family"]
print("at the start : " + str(ranks))
ranks.reverse()
print("after reversing : " + str(ranks))
ranks.sort()
print("after sorting : " + str(ranks))

#WRITING A LOOPS
apes = ["Homo sapiens", "Pan troglodytes", "Gorilla gorilla"]
#printing each element separately
print(apes[0] + " is an ape")
print(apes[1] + " is an ape")
print(apes[2] + " is an ape")
#Statements in loops
apes = ["Homo sapiens", "Pan troglodytes", "Gorilla gorilla"]
for ape in apes: name_length = len(ape)
first_letter = ape[0]
print(ape + " is an ape. Its name starts with " + first_letter)
print("Its name has " + str(name_length) + " letters")

#USING A STRING AS A LIST
name = "martin"
for character in name: print("one character is " + character)

#SPLITTING A STRING TO MAKE A LIST
names = "melanogaster,simulans,yakuba,ananassae"
species = names.split(",")
print(str(species))

#LOOPING WITH RANGES
protein = "vlaspadktnv"
stop_positions = [3,4,5,6,7,8,9,10]
for stop in stop_positions: substring = protein[0:stop]
print(substring)
for number in range(6): print(number)
for number in range(3, 8): print(number)
for number in range(2, 14, 4): print(number)















#####CHAPTER 9 FILES, PROGRAMS, AND USER INPUT
#RENAMING A FILE NAME
import os
import shutil
#os.rename("old.txt", "new.txt")
#MOVE A FILE OR FOLDER
#os.rename("/home/jlreagan/pythonScripts/old.txt, "/home/jlreagan/Desktop/old.txt")
#CREATE MULTIPLE DIRECTORIES AT ONCE
#os.mkdir("/a/long/path/with/lots/of/folders")
#COPY A FILE
#shutil.copy("/home/jlreagan/pythonScripts/old.txt", "/home/jlreagan/old.txt")
#LISTING FOLDER CONTENTS
#for dna.txt in os.listdir("."): print("one file name is " + dna.txt)

#RUNNING A PROGRAM
import subprocess
subprocess.call("/bin/date")
subprocess.call("/bin/date +%B", shell=True)
current_month = subprocess.check_output("/bin/date +%B", shell=True)
dna = "ATCGATCGTGACTAGCTACG"
#accession = input("Enter Accession Name")

#COMMAND LINE ARGUMENTS
import sys
print(sys.argv)