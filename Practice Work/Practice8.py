#square each element 
l=[1,2,3,4,5,6,7,8,9,10]
sqa=list(map(lambda i:i*i,l))
sqa

#Each element into uppercase
names=['harshith','kalipa','gopal']
uppername=list(map(lambda i:i.upper(),names))
uppername

# sort list of dictionaries by key
marks={'python':56,'java':45,'mysql':60,'html':90}
sorted(marks.items(),key=lambda i:i[1])
dict(sorted(marks.items(),key=lambda i:i[1],reverse=True))
marks.items()

#string starts with vowels 
vol='aeiouAEIOU'
check=lambda s:True if s[0] in vol else False
check("apple")
check("banana")

#Multiply each number by its index
l = [1,2,3,4,5,6,7,8,9]
l = list(map(lambda val:val[0]*val[1], enumerate(l)))
print(l)

