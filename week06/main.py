def is_anagram(word1 : str, word2 : str):
    """
    Determine if 'word1' and 'word2' are anagrams.  An anagram
    is when the same letters in a word are re-organized into a 
    new word.  A Python dictionary is used to solve the problem.

    Examples:
    is_anagram("CAT","ACT") would return True
    is_anagram("DOG","GOOD") would return False because GOOD has 2 O's

    Important Note: When determining if two words are anagrams, you
    should ignore any spaces.  You should also ignore cases.  For 
    example, 'Ab' and 'Ba' should be considered anagrams

    Reminder: You can access a letter by index in a Python string by 
    using the [] notation.

    ** CONVERT TO ONE CASE TO MAKE CASE INSENSITIVE **
    
    add letter vals to dictionaty and subtract them from the dictionary
    if any left over its not an anagram    

    CAT = [C, A, T]

    ACT = -A , -C, -T

    
    """
    word_list = lambda words : [word.lower() for word in words if word != ' ']
    word_one  = word_list(word1)
    word_two  = word_list(word2)

    return True if sorted(word_one) == sorted(word_two) else False



# Sample Test Cases (may not be comprehensive) 
print("\n=========== PROBLEM 3 TESTS ===========")
print(is_anagram("CAT","ACT")) # True
print(is_anagram("DOG", "GOOD")) # False
print(is_anagram("AABBCCDD", "ABCD")) # False
print(is_anagram("ABCCD","ABBCD")) # False
print(is_anagram("BC","AD")) # False
print(is_anagram("Ab","Ba")) # True
print(is_anagram("A Decimal Point", "Im a Dot in Place"))  # True
print(is_anagram("tom marvolo riddle", "i am lord voldemort")) # True
print(is_anagram("Eleven plus Two", "Twelve Plus One")) # True
print(is_anagram("Eleven plus One", "Twelve Plus One")) # False