#############
# Problem 4 #
#############

def wildcard_binary(pattern):
    """
    A binary string is a string consisting of 
    just 1's and 0's.  For example, 1010111 is 
    a binary string.  If we introduce a wildcard 
    symbol * into the string, we can say that 
    this is now a pattern for multiple binary 
    strings.  For example, 101*1 could be used 
    to represent 10101 and 10111.  A pattern can
    have more than one * wildcard.  For example, 
    1**1 would result in 4 different binary 
    strings: 1001, 1011, 1101, and 1111.</p>
	
    Using recursion, display all possible binary 
    strings for a given pattern.  You might find 
    some of the Python str functions like find 
    and replace to be useful in solving this problem.

    There should be n^2 results where n is the number of wildcards
    """

    patternChanged = pattern[:]

    if pattern.find("*") == 0:
        print(pattern)
        return
    
    else:
        for i in range(len(pattern)):
            # replace with 0 and recurssion timmeeee boi
            if pattern[i] == "*":
                
                patternChanged[i] = '0'
                wildcard_binary(patternChanged)

                # same thing but with 1
                pattern[i] =  '1'
                wildcard_binary(patternChanged)
                
                
# Sample Test Cases (may not be comprehensive) 
print("\n=========== PROBLEM 4 TESTS ===========")
wildcard_binary("110*0*")
# 110000
# 110001
# 110100
# 110101
wildcard_binary("***")
# 000   
# 001   
# 010
# 011
# 100
# 101
# 110
# 111