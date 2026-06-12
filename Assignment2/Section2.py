# Section 2: Set Challenges 
print("Section 2: Set Challenges")
print("\n\n")

# Q11. Create a set containing 5 numbers and print all elements. 
print("Q11. Create a set containing 5 numbers and print all elements.")
set1 = {1, 2, 3, 4, 5}
print("Elements in the set:")
for i in set1:
    print(i, ",",end="")
print()

# Q12. Add new elements into a set using add(). 
print("Q12. Add new elements into a set using add().")
set1.add(6)
set1.add(7)
print("After adding new elements:")
for i in set1:
    print(i, ",",end="")
print()

# Q13. Remove an element from a set using: 
# - remove() 
# - discard() 
print("Q13. Remove an element from a set using: remove() and discard()")
set1.remove(3)
set1.discard(4)
print("After removing elements:")
for i in set1:
    print(i, ",",end="")
print()

# Q14. Create two sets and perform: 
# - Union 
# - Intersection 
# - Difference 
# operations. 
print("Q14. Create two sets and perform: Union, Intersection, Difference operations.")
setA = {1, 2, 3, 4, 5}
setB = {4, 5, 6, 7, 8}
print("Set A:", setA)
print("Set B:", setB)
print("Union:", setA.union(setB))
print("Intersection:", setA.intersection(setB))
print("Difference (A-B):", setA.difference(setB))
print()

# Q15. Find common elements between two sets. 
print("Q15. Find common elements between two sets.")
common = setA.intersection(setB)
print("Common elements between Set A and Set B:", common)
print()

# Q16. Check whether a particular value exists in a set. 
print("Q16. Check whether a particular value exists in a set.")
product = {"Penicl", "Eraser", "Notebook", "Ruler", "Marker", "Bag"}
print("Products in the set:", product)
search = input("Enter a product name to search: ")
if search in product:
    print(f"{search} is present in the set.")
else:
    print(f"{search} is not present in the set.")
print()

# Q17. Take a list containing duplicate values and convert it into a set. 
print("Q17. Take a list containing duplicate values and convert it into a set.")
my_list = [1, 2, 3, 4, 5, 1, 3, 4, 5, 6, 8, 1]
my_set = set(my_list)
print("Original list:", my_list)
print("Converted set:", my_set)
print()

# Q18. Create a set of student names and display the total number of unique students. 
print("Q18. Create a set of student names and display the total number of unique students.")
students = {"Saquib", "Atharva", "Suraj", "Rohit", "Ishwari", "Chetana"}
print("Unique students:", len(students))
print()

# Q19. Create two sets of numbers and check whether both sets are equal or not. 
print("Q19. Create two sets of numbers and check whether both sets are equal or not.")
setX = {1, 2, 3, 4, 5}
setY = {5, 4, 3, 2, 1}
print("Set X:", setX)
print("Set Y:", setY)
if setX == setY:
    print("EQUAL")
else:
    print("UNEQUAL")
print()

# Q20. Remove all elements from a set using clear(). 
print("Q20. Remove all elements from a set using clear().")
setX.clear()
print("After clearing setX:", setX)