#7.1 Tuple Execution

#Indexing

my_tuple = (10,20,30,40)
print(my_tuple[2]) #Output: 30

#Negative Indexing

my_tuple = (10, 20, 30, 40)
print(my_tuple[-1]) #Output: 40

#Slicing

my_tuple = (10, 20, 30, 40, 50)
print(my_tuple[1:4]) #Output: (20, 30, 40)

#Concatination

tuple1 = (1, 2)
tuple2 = (3, 4)
new_tuple = tuple1 + tuple2 #Output: (1, 2, 3, 4)

#Repetition

my_tuple = (1, 2)
print(my_tuple * 3) #Output: (1, 2, 1, 2, 1, 2)

#Membership Testing

my_tuple = (1, 2, 3)
print(2 in my_tuple) #Output: True
print(5 not in my_tuple) #Output: True

#Tuple Unpacking

my_tuple = (1, 2, 3)
a, b, c = my_tuple
print(a, b, c) #Output: 1 2 3

#Count(x)

print((1,2,2,3).count(2)) #Output: 2

#Index(x)

print((1, 2, 3).index(2)) #Output: 1

#Len(tuple)

print(len((1, 2, 3))) #Output: 3

#max(tuple)

print(max((1, 2, 3))) #Output: 3

#min(tuple)

print(min((1, 2, 3))) #Output: 1

#sum(tuple)

print(sum((1, 2, 3))) #Output: 6

#tuple(iterable)

print(tuple([1, 2, 3])) #Output: (1, 2, 3)

