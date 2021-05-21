"""
CSE212 
(c) BYU-Idaho
05-Prove - Problem 2

It is a violation of BYU-Idaho Honor Code to post or share this code with others or 
to post it online.  Storage into a personal and private repository (e.g. private
GitHub repository, unshared Google Drive folder) is acceptable.
"""

def find_pairs(words):
    """
    The words parameter contains a list of two character 
    words (lower case, no duplicates). Using sets, find an O(n) 
    solution for displaying all symmetric pairs of words.  

    For example, if words was: [am, at, ma, if, fi], we would display:

    am & ma
    if & fi

    The order of the display above does not matter.  'at' would not 
    be displayed because 'ta' is not in the list of words.

    As a special case, if the letters are the same (example: 'aa') then
    it would not match anything else (remember no the assumption above
    that there were no duplicates) and therefore should not be displayed.
    """    
    """
    FOR value in values
        IF value[::-1] is MEMBER of set
            print(value) + "&" + print(value[::-1])
            print(f"{value} & {value[set1]}" ,end="")
            Deal with formatting with multiple outputs and 
    """

    set1 = set()
    for value in words:
        if value[::-1] in set1: # is in words
            print(f"{value} & {value[::-1]}")
        set1.add(value)   
    pass

find_pairs(["am","at","ma","if","fi"])      # ma & am, fi & if
print("=============")
find_pairs(["ab", "bc", "cd", "de", "ba"])  # ba & ab
print("=============")
find_pairs(["ab","ba","ac","ad","da","ca"]) # ba & ab, da & ad, ca & ac
print("=============")
find_pairs(["ab", "ac"])                    # None
print("=============")
find_pairs(["ab", "aa", "ba"])              # ba & ab
print("=============")
find_pairs(["23","84","49","13","32","46","91","99","94","31","57","14"])
                                            # 32 & 23, 94 & 49, 31 & 13