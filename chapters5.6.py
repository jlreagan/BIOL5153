#####CHAPTER  Writing a function

#Defining a function
	
def get_at_content(dna):
	length = len(dna)
	a_count = dna.upper().count('A')
	t_count = dna.upper().count('T')
	at_content = (a_count + t_count) / length
	return round(at_content, 2)
	#return at_content will give all numbers
	#return round(at_content, 2) will round to 2 sigfigs

get_at_content("ATGACTGGACCA")
my_at_content = get_at_content("ATGCGCGATCGATCGAATCG")
print("AT content is " + str(get_at_content("ATGACTGGACCA")))
print(str(my_at_content))
print(get_at_content("ATGCATGCAACTGTAGC"))
print(get_at_content("aactgtagctagctagcagcgta"))

#Defining a function without an argument
def get_a_number():
	return 42
	
#calling functions with named arguments
#get_at_content("ATCGTGACTCG", 2)
#get_at_content(dna="ATCGTGACTCG", sig_figs=2)
#identical statements:
#get_at_content(dna="ATCGTGACTCG", sig_figs=2)
#get_at_content(sig_figs=2, dna="ATCGTGACTCG")

#get_at_content("ATCGTGACTCG")
#get_at_content("ATCGTGACTCG", 3)
#get_at_content("ATCGTGACTCG", sig_figs=4)