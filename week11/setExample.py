# Creating and defining a set

thisSet = {"apple", "banana", "cherry", "apple"}

# Creating Empty Sets
emptySet = set()

print(thisSet)
print(emptySet)


# Apending to a Set
set1 = {"apple", "banana", "cherry"}

# Use the .append method to add items
set1.append("grapes")

print(set1)


# Finding the Length of a Set
set1 = {"apple", "banana", "cherry"}

# Use the len() function to find the length of a set
# There are 3 items in the list. What is the result of the print statement?
Print((len(set1))


# Set Unions
# Union using "|" symbol

set1 = {"apple", "banana", "cherry"}
set2 = {"onion", "potato", "carrot"}

# Print union
print(set1 | set2)

# Union using ".union" method

set1 = {"apple", "banana", "cherry"}
set2 = {"onion", "potato", "carrot"}

# Print union
print(set1.union(set2))


# Set Intersections
# Intersection using "- " symbol

set1 = {"apple", "banana", "cherry", "onion"}
set2 = {"onion", "potato", "carrot", "apple"} 

# Print Intersection
print(set1 - set2)


