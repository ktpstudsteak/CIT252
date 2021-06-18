def permutations(letters, word=""):

	if len(letters) == 0:   # Base Case
		print(word)  

	else:
		# Try adding each of the available letters
		# to the 'word_so_far' and add up all the
		# resulting permutations.

		for index in range(len(letters)):
			# Make a copy of the letters to pass to the
			# the next call to permutations.  We need
			# to remove the letter we just added before
			# we call permutations again.

			letters_left = letters[:]
			del letters_left[index]

			# Add the new letter to the word we have so far
			permutations(letters_left, word + letters[index])

permutations(list("ABC"))
""" 
Results:
ABC
ACB
BAC
BCA
CAB
CBA
"""

permutations(list("ABCD"))
"""
Results:
ABCD
ABDC
ACBD
ACDB
ADBC
ADCB
BACD
BADC
BCAD
BCDA
BDAC
BDCA
CABD
CADB
CBAD
CBDA
CDAB
CDBA
DABC
DACB
DBAC
DBCA
DCAB
DCBA
"""