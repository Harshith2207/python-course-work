#9. Type Conversion

#1.int conversion
int_a = 2
print(float(int_a))   # Output: 2.0
print(str(int_a))     # Output: '2'
print(bool(int_a))    # Output: True
# The below would raise errors if uncommented
# print(list(int_a))   # TypeError

#2.float conversion
float_n = 3.1
print(int(float_n))   # Output: 3
print(str(float_n))   # Output: '3.1'
print(bool(float_n))  # Output: True

#3.str conversion
string_c = 'power'
print(int('10'))       # Output: 10
# print(int('10.9'))   # ValueError
# print(int('power'))  # ValueError
print(float('10.8'))   # Output: 10.8
print(bool(string_c))  # Output: True
print(list(string_c))  # Output: ['p', 'o', 'w', 'e', 'r']
print(tuple(string_c)) # Output: ('p', 'o', 'w', 'e', 'r')
print(set(string_c))   # Output: {'e', 'w', 'r', 'o', 'p'}

#4.list conversion
list_d = [1, 2, 3, 4]
print(str(list_d))     # Output: "[1, 2, 3, 4]"
print(bool(list_d))    # Output: True
print(tuple(list_d))   # Output: (1, 2, 3, 4)
print(set(list_d))     # Output: {1, 2, 3, 4}

#5.tuple conversion
tuple_f = (1, 2, 3, 4)
print(str(tuple_f))    # Output: "(1, 2, 3, 4)"
print(bool(tuple_f))   # Output: True
print(list(tuple_f))   # Output: [1, 2, 3, 4]
print(set(tuple_f))    # Output: {1, 2, 3, 4}

#6.set conversion
set_e = {3, 4, 5, 6}
print(str(set_e))      # Output: '{3, 4, 5, 6}'
print(bool(set_e))     # Output: True
print(list(set_e))     # Output: [3, 4, 5, 6] (Order may vary)
print(tuple(set_e))    # Output: (3, 4, 5, 6)

#7.dict conversion
dict_g = {1: 1, 2: 4, 3: 9}
print(str(dict_g))     # Output: '{1: 1, 2: 4, 3: 9}'
print(bool(dict_g))    # Output: True
print(list(dict_g))    # Output: [1, 2, 3]
print(tuple(dict_g))   # Output: (1, 2, 3)
print(set(dict_g))     # Output: {1, 2, 3}

#8.bool conversion
boolean = False
print(int(boolean))    # Output: 0
print(float(boolean))  # Output: 0.0
print(str(boolean))    # Output: 'False'

boolean = True
print(int(boolean))    # Output: 1
print(float(boolean))  # Output: 1.0
print(str(boolean))    # Output: 'True'

#9.Dict conversion(list of tuples)
d = [('name', 'harshith'), ('batch', '14'), ('subject', 'python')]
converted_dict = dict(d)
print(converted_dict) # Output: {'name': 'harshith', 'batch': '14', 'subject': 'python'}
