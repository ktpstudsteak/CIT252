# Sets

## What are sets?
Sets are a data structure for storing multiple items in a single variable.

They are declared using curly braces.

Sets cannot have duplicates, and if any are inputted, it will automatically remove duplicates.

Sets compare their items using *hashing*.

Remember, sets are **unordered**,  **unindexed**, and **unchangeable**.
<br />

## Set use cases
If you have multiple items you need to store without having to care about order, use a set. 

![Python Set Picture](https://static.thegeekstuff.com/wp-content/uploads/2019/04/python-set.png)

<br />

## Performance
Because sets hash their items when comparing, it is extremely efficiant and has a BigO of O(1).

## Examples

See `setExample.py` for examples. Feel free to play around with them!

<br />

## Problem
Write a set called `snacks` that includes at least 3 of your favorite snack foods.

See `setProblem.py` if you get stuck.