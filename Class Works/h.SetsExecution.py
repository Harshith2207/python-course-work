#8. Sets Execution

# Creating a set with unique elements
my_set = {1, 2, 3, 4}
my_set

# Creating an empty set (use set() function, not {})
empty_set = set()

# Set with duplicate elements (duplicates are removed automatically)
set_with_duplicates = {1, 2, 2, 3, 4}
print(set_with_duplicates) # Output: {1, 2, 3, 4}

#Set Properties

#Operations on Sets :

#Membership Testing

my_set = {1, 2, 3, 4}
print(3 in my_set) # Output: True
print(5 not in my_set) # Output: True

#Union (| or union() method)

set1 = {1, 2, 3}
set2 = {3, 4, 5}
result = set1 | set2 # Output: {1, 2, 3, 4, 5}

#Intersection (& or intersection() method)

set1 = {1, 2, 3}
set2 = {3, 4, 5}
result = set1 & set2 # Output: {3}

#Difference (- or difference() method)

set1 = {1, 2, 3}
set2 = {3, 4, 5}
result = set1 - set2 # Output: {1, 2}

#Symmetric Difference (^ or symmetric_difference() method)

set1 = {1, 2, 3}
set2 = {3, 4, 5}
result = set1 ^ set2 # Output: {1, 2, 4, 5}

#Subset (<= or issubset() method)

set1 = {1, 2}
set2 = {1, 2, 3}
print(set1 <= set2) # Output: True

#Superset (>= or issuperset() method)

set1 = {1, 2, 3}
set2 = {1, 2}
print(set1 >= set2) # Output: True

#Disjoint Sets (isdisjoint() method)

set1 = {1, 2, 3}
set2 = {4, 5, 6}
print(set1.isdisjoint(set2)) # Output: True

#Built-in Methods for Sets

# 1. add(element)
s = {1, 2, 3}
s.add(4)
print(s)  # {1, 2, 3, 4}

# 2. remove(element)
s = {1, 2, 3}
s.remove(2)
print(s)  # {1, 3}

# 3. discard(element)
s = {1, 2, 3}
s.discard(5)
print(s)  # {1, 2, 3} → No error

# 4. pop()
s = {10, 20, 30}
s.pop()
print(s)  # Removes a random element

# 5. clear()
s = {1, 2, 3}
s.clear()
print(s)  # set()

# 6. union(other_set)
a = {1, 2}
b = {2, 3}
print(a.union(b))  # {1, 2, 3}

# 7. intersection(other_set)
a = {1, 2, 3}
b = {2, 3, 4}
print(a.intersection(b))  # {2, 3}

# 8. difference(other_set)
a = {1, 2, 3}
b = {2, 3}
print(a.difference(b))  # {1}

# 9. symmetric_difference(other_set)
a = {1, 2, 3}
b = {3, 4}
print(a.symmetric_difference(b))  # {1, 2, 4}

# 10. update(other_set)
a = {1, 2}
b = {2, 3}
a.update(b)
print(a)  # {1, 2, 3}

# 11. intersection_update(other_set)
a = {1, 2, 3}
b = {2, 3, 4}
a.intersection_update(b)
print(a)  # {2, 3}

# 12. difference_update(other_set)
a = {1, 2, 3}
b = {2}
a.difference_update(b)
print(a)  # {1, 3}

# 13. symmetric_difference_update(other_set)
a = {1, 2, 3}
b = {2, 4}
a.symmetric_difference_update(b)
print(a)  # {1, 3, 4}

# 14. copy()
a = {1, 2}
b = a.copy()
print(b)  # {1, 2}

# 15. isdisjoint(other_set)
a = {1, 2}
b = {3, 4}
print(a.isdisjoint(b))  # True

# 16. issubset(other_set)
a = {1, 2}
b = {1, 2, 3}
print(a.issubset(b))  # True

# 17. issuperset(other_set)
a = {1, 2, 3}
b = {1, 2}
print(a.issuperset(b))  # True

#Built-in Functions for Sets

# 1. len(set)
s = {10, 20, 30}
print(len(s))  # 3

# 2. max(set)
s = {5, 10, 2}
print(max(s))  # 10

# 3. min(set)
s = {5, 10, 2}
print(min(s))  # 2

# 4. sum(set)
s = {1, 2, 3}
print(sum(s))  # 6

# 5. sorted(set)
s = {3, 1, 2}
print(sorted(s))  # [1, 2, 3]

# 6. set(iterable)
lst = [1, 2, 2, 3]
s = set(lst)
print(s)  # {1, 2, 3}

#Immutability & Frozensets
frozen = frozenset([1, 2, 3])
print(frozen) #frozenset({1, 2, 3})
















