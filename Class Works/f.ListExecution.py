#6. List Execution

#Basic Features of Lists-(Ordered,Mutuable,Indexed,Allow Duplicates,Heterogeneous,Dynamic)

l=[1,2,3,4,5,6,7]
l #[1, 2, 3, 4, 5, 6, 7]
l.append(8)
l #[1, 2, 3, 4, 5, 6, 7, 8]
l.remove(1)
l #[2, 3, 4, 5, 6, 7, 8]
l[2] #4
l[5] #7
l #[2, 3, 4, 5, 6, 7, 8]

#Adding Elements

l.append(2)
l #[2, 3, 4, 5, 6, 7, 8, 2]
l.append(2.3)
l.append("string")
l.append(True)
l.append((1,2,3))
l.append({1,2,3})
l.append({"course":"py"})
l.append(2+5j)
l.append([1,2,3])
l #[2, 3, 4, 5, 6, 7, 8, 2, 2.3, 'string', True, (1, 2, 3), {1, 2, 3},{'course': 'py'}, (2+5j), [1, 2, 3]]
l=[]
l=list()
'''[2, 3, 4, 5, 6, 7, 8, 2, 2.3, 'string', True, (1, 2, 3), {1, 2, 3},
{'course': 'py'}, (2+5j), [1, 2, 3]]'''
l=[2, 3, 4, 5, 6, 7, 8, 2, 2.3, 'string', True, (1, 2, 3), {1, 2, 3}, {'course': 'py'}, (2+5j), [1, 2, 3]]
l[-3:] #[{'course': 'py'}, (2+5j), [1, 2, 3]]
l[:7] #[2, 3, 4, 5, 6, 7, 8]
l[8:10] #[2.3, 'string']
l[9:11] #['string', True]
len(l) #16
l[-7:-11] #[]
l[-7:-11:-1] #['string', 2.3, 2, 8]
l[-6:-10:-1] #[True, 'string', 2.3, 2]
l[::-1]
'''[[1, 2, 3], (2+5j), {'course': 'py'}, {1, 2, 3}, (1, 2, 3), True,
'string', 2.3, 2, 8, 7, 6, 5, 4, 3, 2]'''
l[0] #2
l[0]=l
l
'''[2, 3, 4, 5, 6, 7, 8, 2, 2.3, 'string', True,
(1, 2, 3), {1, 2, 3}, {'course': 'py'}, (2+5j), [1, 2, 3]]'''

l.append("append function")
l
'''[1, 3, 4, 5, 6, 7, 8, 2, 2.3, 'string', True, (1, 2, 3), {1, 2, 3},
{'course': 'py'}, (2+5j), [1, 2, 3], 'append function']'''
l.extend(["extend start",1,2,3,'extend end'])
l
'''[1, 3, 4, 5, 6, 7, 8, 2, 2.3, 'string', True, (1, 2, 3), {1, 2, 3}, {'course': 'py'},
(2+5j),[1, 2, 3], 'append function', 'extend start', 1, 2, 3, 'extend end']'''
l.insert(1,2)
l
'''[1, 2, 3, 4, 5, 6, 7, 8, 2, 2.3, 'string', True, (1, 2, 3), {1, 2, 3}, {'course': 'py'},
(2+5j), [1, 2, 3], 'append function', 'extend start', 1, 2, 3, 'extend end']'''

#Removing Elements

l.remove(True)
l
'''[2, 3, 4, 5, 6, 7, 8, 2, 2.3, True, (1, 2, 3), {1, 2, 3}, {'course': 'py'}, (2+5j),
[1, 2, 3], 'append function', 'extend start', 1, 2, 3, 'extend end']'''
l.remove((2+5j))
l
'''[2, 3, 4, 5, 6, 7, 8, 2, 2.3, True, (1, 2, 3),
{1, 2, 3}, [1, 2, 3], 'append function', 'extend start', 1, 2, 3, 'extend end']'''
l.pop() #'extend end'
l
'''[2, 3, 4, 5, 6, 7, 8, 2, 2.3, True, (1, 2, 3), {1, 2, 3}, [1, 2, 3], 'append function', 'extend start', 1, 2, 3]'''
l.pop() #3
l.pop() #2
l.pop() #1
l.pop() #'extend start'
l #[2, 3, 4, 5, 6, 7, 8, 2, 2.3, True, (1, 2, 3), {1, 2, 3}, [1, 2, 3], 'append function']
l.pop(8) #2.3
l.pop(8) #True
l #[2, 3, 4, 5, 6, 7, 8, 2, (1, 2, 3), {1, 2, 3}, [1, 2, 3], 'append function']
del l[-1]
l #[2, 3, 4, 5, 6, 7, 8, 2, (1, 2, 3), {1, 2, 3}, [1, 2, 3]]

del l[-2] #l
l #[2, 3, 4, 5, 6, 7, 8, 2, (1, 2, 3), [1, 2, 3]]
l.remove(2)
l #[3, 4, 5, 6, 7, 8, 2, (1, 2, 3), [1, 2, 3]]
l.pop(0) #3
l.pop(0) #4
l #[5, 6, 7, 8, 2, (1, 2, 3), [1, 2, 3]]
l.pop() #[1, 2, 3]
l.pop() #(1, 2, 3)
l.pop() #2
l.pop(0) #5

del l[0]
l=[1,2,3]
l.clear()
l #[]
l=[1,2,3]
del l #l
l=[1,2,3,5]
l.index(5) #3
l=[2, 3, 4, 5, 6, 7, 8, 2, 2.3, True, (1, 2, 3),
{1, 2, 3}, [1, 2, 3], 'append function', 'extend start', 1, 2, 3, 'extend end']
l.index('append function') #13
l.count(2) #3
l=[4,2,3,5,6,1,2,3,7,4,9,8,7,6,4,2]
sorted(l) #[1, 2, 2, 2, 3, 3, 4, 4, 4, 5, 6, 6, 7, 7, 8, 9]
l #[4, 2, 3, 5, 6, 1, 2, 3, 7, 4, 9, 8, 7, 6, 4, 2]
l.sort()
l #[1, 2, 2, 2, 3, 3, 4, 4, 4, 5, 6, 6, 7, 7, 8, 9]
l.sort(reverse=True)
l #[9, 8, 7, 7, 6, 6, 5, 4, 4, 4, 3, 3, 2, 2, 2, 1]
l.reverse()
l #[2, 4, 6, 7, 8, 9, 4, 7, 3, 2, 1, 6, 5, 3, 2, 4]
l[::-1] #[4, 2, 3, 5, 6, 1, 2, 3, 7, 4, 9, 8, 7, 6, 4, 2]
l #[2, 4, 6, 7, 8, 9, 4, 7, 3, 2, 1, 6, 5, 3, 2, 4]

#Sorting & Reversing Lists

l.reverse()
l=[1,2,3,4]
k=l.copy()
k.append(5)
l #[1, 2, 3, 4]
k #[1, 2, 3, 4, 5]
m=l
m.append(6)
m #[1, 2, 3, 4, 6]
l #[1, 2, 3, 4, 6]
l.index(2) #1
l #[1, 2, 3, 4, 6]

max(l) #6
min(l) #1
sum(l) #16
l=[23.2,23.4]
l #[23.2, 23.4]
sum(l) #46.599999999999994
len(l) #2
any(l) #True
all(l) #True
l=[2, 3, 4, 5, 6, 7, 8, 2, 2.3, True, (1, 2, 3), {1, 2, 3},
[1, 2, 3], 'append function', 'extend start', 1, 2, 3, 'extend end']
all(l) #True
l.append(0)
l
'''[2, 3, 4, 5, 6, 7, 8, 2, 2.3, True, (1, 2, 3), {1, 2, 3},
[1, 2, 3], 'append function', 'extend start', 1, 2, 3, 'extend end', 0]'''
all(l) #False













