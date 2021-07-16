# Sets

## What are sets?
Sets are a data structure for storing multiple items in a single variable.

They are declared using curly braces.

Sets cannot have duplicates, and if any are inputted, it will automatically remove duplicates.

Sets compare their items using *hashing*.

Remember, sets are **unordered**,  **unindexed**, and the items in them are **unchangeable**.
<br />

## Set use cases
If you have multiple items you need to store without having to care about order, use a set. 

Adding items to the list can be done with the `.append` method.

Length of a set can be determined with the `len()` function.

To make a union of sets, wherein sets are combined together, use the `|` symbol, or with the `.union` method.

You can also find intersections in sets, where the sets have items in common. This can be done with the `-` symbole and the `.difference` method.

These will all be demonstrated in the example section and in [setExample.py](./setExample.py).

![Python Set Picture](https://static.thegeekstuff.com/wp-content/uploads/2019/04/python-set.png)

<br />

## Performance
Because sets hash their items when comparing, it is extremely efficiant and has a BigO of O(1).

## Examples

``` python
# Creating and defining a set

thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)

```

``` python
# Union using "|" symbol

set1 = {"apple", "banana", "cherry"}
set2 = {"onion", "potato", "carrot"}

# Print union
print(set1 | set2)
```

``` python
# Union using ".union" method

set1 = {"apple", "banana", "cherry"}
set2 = {"onion", "potato", "carrot"}

# Print union
print(set1.union(set2))

```

``` python
# Intersection using "- " symbol

set1 = {"apple", "banana", "cherry", "onion"}
set2 = {"onion", "potato", "carrot", "apple"}

# Print Intersection
print(set1 - set2)
```

``` python
# Intersection using ".difference" method

set1 = {"apple", "banana", "cherry", "onion"}
set2 = {"onion", "potato", "carrot", "apple"}

# Print union
print(set1.difference(set2))

```

Notice how the unions combine both sets and intersections find thier common parts. 


<br />

## Problem
Write a set called `snacks` that includes at least 3 of your favorite snack foods.

See [setProblem.py](./setProblem.py) if you get stuck.