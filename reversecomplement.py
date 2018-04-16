#Reversecomplement.py

dna=("ACTGAT")

dna= dna.upper

print (dna)

a_count = dna.count ('A')
t_count = dna.count ('T')
g_count = dna.count ('G')
c_count = dna.count ('C')

dna_length = len (dna)
gc = (g_count+c_count)/dna_length
at = (a_count+t_count)/dna_length
print("%.2f" % gc)
#print("%.2f" % at)

compA1=(dna.replace("A", "t"))
compT1=(compA1.replace("T","a"))
compC1=(compT1.replace("C", "g"))
compG1=(compC1.replace("G", "c"))

dna_comp = compG1.upper()
dna_comp = dna_comp [::-1]
print("%.2f" % ((comp_g_count+comp_c_count)/dna_length))

#print(dna_length)
#print(a_count
#print(c_count)
#print(g_count)
#print(t_count)

