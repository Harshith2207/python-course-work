'''
import sys
a=10
b=20
print(a+b)
sys.exit()
print(a-b)
'''

'''
import platform as pf
print(pf.system())
print(pf.release())
print(pf.processor())
'''

'''
import math
print(math.sqrt(25))
print(math.pow(2,3))

#round means nearer value
print(round(12.3))
print(round(12.8))

#ceil means upper value/upper value
print(math.ceil(12.3))

#floor means lower/downer value
print(math.floor(13.5))

#fabs - absolute value is without -ve value
print(math.fabs(12))

#gcd - greatest common factor
print(math.gcd(8,24))

print(math.sin(45))
print(math.cos(0))
print(math.tan(45))

print(math.degrees(45))
print(math.radians(30))
'''

'''
import random
random.seed(12)
print(random.random())
print(random.randint(4,8))
print(random.uniform(3,6))
names=['varun','arun','karun','tarun']
print(random.choice(names))
print(random.choices(names))
print(random.shuffle(names))
'''

'''
#counter used to count
import collections
w='python program java program html file css file'.split()
d=collections.Counter(w)
print(d)

#defaultdict provides default values
s = 'abcdef'
d = collections.defaultdict(str)
for index, char in enumerate(s):
    d[char]+=str(index)
print(dict(d))


from collections import deque
d = deque('abc')  # deque(['a', 'b', 'c'])
d.append('d')     # deque(['a', 'b', 'c', 'd'])
d.appendleft('z') # deque(['z', 'a', 'b', 'c', 'd'])
d.pop()           # 'd', deque(['z', 'a', 'b', 'c'])
d.popleft()       # 'z', deque(['a', 'b', 'c'])
d.rotate(1)       # deque(['c', 'a', 'b'])
d.rotate(-1)      # deque(['a', 'b', 'c'])
print(d)          # deque(['a', 'b', 'c'])
'''

'''
from itertools import combinations,permutations
print(list(combinations('ABCD', 2)))
print(list(permutations('ABCD', 2)))
'''

from datetime import date,time,datetime,timedelta
today=date.today()
print(today)
print(today.year)
print(today.month)
print(today.day)
print(today.weekday())
print(today.isoweekday())

d = date(2025,8,7)
t = time(14, 30, 15) # 14:30:15 (2:30:15 PM)
dt=datetime(2024,2,16,14,30,15)

now=datetime.now()
print(now)
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)

print(now.strftime('%Y-%m-%d'))
print(now.strftime('%d %b, %Y'))
print(now.strftime('%d-%b-%y %H:%M:%S'))

fdate=today - timedelta(days=7)



