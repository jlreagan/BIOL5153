#! /usr/bin/env python3
# from Bio import SeqIO
featureLines=[]
featuresplit= []

fastaFile = input("Enter FASTA.file Name ")

# for record in SeqIO.parse(fastaFile, "fasta"):
	# seq = record.seq
	# print (seq)
	
lines = open(fastaFile).readlines()
seq = (lines[1])

GFFFile = input("Enter GFF File Name ")
feature = input ("Enter feature type ")

GFFlines = open(GFFFile).readlines()


for i in range(0, len(GFFlines)):
	if GFFlines[i].find(feature) != -1:
		featureLines.append(GFFlines[i])
		print (GFFlines[i])
		
		
for feature in featureLines:
	#feature.split()
	#print (feature.split())
	
	featuresplit.append(feature.split())

for item in featuresplit:
	print (str(item[0:2])+str(item[9:11]))
	start = item[4]
	stop = item[5]
	print (seq[int(start):int(stop)])