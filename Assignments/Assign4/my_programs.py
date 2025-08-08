def reverse_string():
    print("Program: Reverse a String (Without [::-1] or reversed())")
    print("""
def reverse_str(s):
    result = ''
    for char in s:
        result = char + result
    return result
    """)
    print("Test Case 1: reverse_str('hello') → 'olleh'")
    print("Test Case 2: reverse_str('abc') → 'cba'")
    print("Explanation: Characters are prepended one by one to reverse the string.\n")

def char_frequency():
    print("Program: Character Frequency Counter")
    print("""
def count_freq(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return freq
    """)
    print("Test Case 1: count_freq('hello') → {'h':1, 'e':1, 'l':2, 'o':1}")
    print("Test Case 2: count_freq('aabb') → {'a':2, 'b':2}")
    print("Explanation: We use a dictionary to count occurrences of each character.\n")

def remove_duplicates():
    print("Program: Remove Duplicates from List (Without set())")
    print("""
def remove_dups(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result
    """)
    print("Test Case 1: remove_dups([1, 2, 2, 3]) → [1, 2, 3]")
    print("Test Case 2: remove_dups(['a', 'a', 'b']) → ['a', 'b']")
    print("Explanation: Only add elements to result if not already present.\n")

def common_elements():
    print("Program: Find Common Elements in Two Lists")
    print("""
def common(lst1, lst2):
    return [item for item in lst1 if item in lst2]
    """)
    print("Test Case 1: common([1,2,3], [2,3,4]) → [2,3]")
    print("Test Case 2: common(['a','b'], ['b','c']) → ['b']")
    print("Explanation: We use list comprehension to filter elements in both lists.\n")

def merge_dictionaries():
    print("Program: Merge Two Dictionaries")
    print("""
def merge_dicts(d1, d2):
    return {**d1, **d2}
    """)
    print("Test Case 1: merge_dicts({'a':1}, {'b':2}) → {'a':1, 'b':2}")
    print("Test Case 2: merge_dicts({'x':10}, {'x':20, 'y':30}) → {'x':20, 'y':30}")
    print("Explanation: Dictionary unpacking merges the contents, with latter keys overwriting.\n")

def simple_calculator():
    print("Program: Simple Calculator Using Functions")
    print("""
def calculate(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a / b
    else:
        return 'Invalid operator'
    """)
    print("Test Case 1: calculate(10, 5, '+') → 15")
    print("Test Case 2: calculate(6, 2, '*') → 12")
    print("Explanation: Use conditional statements to handle operator-based arithmetic.\n")

def sort_tuples_by_second():
    print("Program: Sort List of Tuples by Second Element")
    print("""
def sort_by_second(lst):
    return sorted(lst, key=lambda x: x[1])
    """)
    print("Test Case 1: sort_by_second([(1,3), (2,2), (3,1)]) → [(3,1), (2,2), (1,3)]")
    print("Test Case 2: sort_by_second([('a',5), ('b',3)]) → [('b',3), ('a',5)]")
    print("Explanation: We use `sorted()` with key as the second item in each tuple.\n")

def flatten_nested_list():
    print("Program: Flatten a Nested List")
    print("""
def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result
    """)
    print("Test Case 1: flatten([[1, 2], [3, [4]]]) → [1, 2, 3, 4]")
    print("Test Case 2: flatten([1, [2, [3, [4]]]]) → [1, 2, 3, 4]")
    print("Explanation: Recursively flatten sublists and append to result list.\n")

def missing_number():
    print("Program: Find the Missing Number in a List")
    print("""
def find_missing(lst, n):
    total = n * (n + 1) // 2
    return total - sum(lst)
    """)
    print("Test Case 1: find_missing([1,2,4,5], 5) → 3")
    print("Test Case 2: find_missing([1,3], 3) → 2")
    print("Explanation: Use sum formula of 1 to N and subtract actual sum of list.\n")

def check_anagram():
    print("Program: Check if Two Strings are Anagrams")
    print("""
def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)
    """)
    print("Test Case 1: is_anagram('listen', 'silent') → True")
    print("Test Case 2: is_anagram('hello', 'world') → False")
    print("Explanation: Sort both strings and compare equality to check anagram.\n")
