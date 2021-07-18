"""

Write a set called `snacks` that includes at least 3 of your favorite snack foods. 

Append 3 more snacks.

Create another set with a name of your choice and add at least 3 new items.

Make a union with both sets.

"""

# Problem Solution:

snacks = {"Doritos", "gummi bears", "Bacon flavored sunflower seeds"}

print("My favorite snacks are: " + favSnacks)

vegtables = {"onion", "tomato", "potato", "carrot"}

food = snacks|vegtables

print(food)