#5. String Execution

#1.Operations on Strings

#Concatenation(+)-Joining two or more strings

fname='Harshith'
lname='Vemana'
fname+lname #'HarshithVemana'

#Repetition(*)-Repeating a string multiple times

fname*3 #'HarshithVemanaHarshithVemanaHarshithVemana'
fname #'HarshithVemana'

#Indexing-Accessing individual char using indices

s='Python Programming'
s[5] #'n'
s[1] #'y'
s[-3] #'i'
s[5] #'n'

#Slicing-Extracting a part(substring)of the strin

names='HarshithSoumyaKiranVarunMani'
names #'HarshithSoumyaKiranVarunMani'
#[start:end+1:step]
names[0:8] #'Harshith'
names[8:14] #'Soumya'
names[14:19] #'Kiran'
names[19:24] #'Varun'
names[24:28] #'Mani'
names[0:8:2] #'Hrht'
names[0:28:1] #'HarshithSoumyaKiranVarunMani'
names[0:28:2] #'HrhtSwyKrnauMn'
names[1:28:2] #'asihomaiaVrnai'
names[-5:-1] #'nMan'
names[-4:] #'Mani'
names[-27:-14] #'arshith'
names[:-20] #'Harshith'
names[::-1] #'inaMnuraVnariKaymwoShtihsraH'
names #'HarshithSoumyaKiranVarunMani'
names[-1:-4:-1] #'ina'
names[-1:-5:-1] #'inam'
names[-10:-15:-1] #'narik'

#Membership(in,not in)

names #'HarshithSoumyaKiranVarunMani'
'Kiran' in names #True
'Adithya' in names #False
'Hema' not in names #True
'Mounica' not in names #True

#2.Built-in String Func

#len()-Return the length of the string

names #'HarshithSoumyaKiranVarunMani'
len(names) #28

#max()/min()-Returns the maximum or minimum character (based on ASCII values)

max(names) #'y'
min(names) #'H'

#Sorted()-Returns a sorted list of characters.

sorted('names') #['H', 'K', 'M', 'S', 'V', 'a', 'a', 'a', 'a', 'a', 'h', 'h', 'i', 'i', 'i', 'm', 'n', 'n', 'n', 'o', 'r', 'r', 'r', 's', 't', 'u', 'w', 'y']

#chr()/ord()-Converts between characters and their ASCII codes

ord('H') #72
ord('K') #75
ord('S') #83
ord('a') #97
chr(97) #'a'
chr(1) #'\x01'
chr(30) #'\x1e'
chr(101) #'e'
chr(120) #'x'
ord('1') #49
ord('9') #57
ord('@') #64

#Python StringMethods
#1.Case Conversion Methods

#upper()-Converts all characters to uppercase

names #'HarshithSoumyaKiranVarunMani'
names.upper() #'HARSHITHSOUMYAKIRANVARUNMANI'

#lower()-Converts all characters to lowercase

names.lower() #'harshithsoumyakiranvarunmani'

#title()-Capitalizes the first letter of each word

d='python programming lang'
d.title() #'python programming lang'
d #'python programming lang'

#capitalize()-Capitalizes the first character

d.capitalize() #'Python programming lang'
d #'python programming lang'

#swapcase() Swaps case: upper → lower, lower → upper

names #'HarshithSoumyaKiranVarunMani'
names.swapcase() #'hARSHITHsOUMYAkIRANvARUNmANI'

#casefold()-Converts to lowercase (more aggressive than lower())

'ß'.casefold() #'ss'
'ß'.lower() #'ß'

#2.Alignment & Formatting Methods
#center(width,fillchar)

d #'python programming lang'
d.center(50,'-') #'-------------python programming lang--------------'
d.center(50,'*') #'*************python programming lang**************'
d.center(50,' ') #'             python programming lang              '

#ljust(width,fillchar)

d.ljust(50,'_') #'python programming lang___________________________'
"name".ljust(10,' ') #'name      '

#rjust(width,fillchar)

d.rjust(50,'_') #'___________________________python programming lang'

#zfill(width)

'42'.zfill(5) #'00042'
'301'.zfill(2) #'301'
'301'.zfill(5) #'00301'
'4321'.zfill(5) #'04321'

#3.Search & Find Methods
#find(sub)-Returns the index of first occurrence, -1 if not found

names #'HarshithSowmyaKiranVarunMani'
names.find("kiran") #-1
names.find("Kiran") #14
names.find(names[:8]) #0
names.find(names[14:19]) #14
names.find('z') #-1
names.find('H') #0
names.find('S') #8
names.find('a') #1

#rfind(sub)-Returns the last occurrence of the substring

names.rfind('a') #25

#index(sub)-Like find(), but raises an error if not found

names.index('S') #8

#count(sub)-Counts how many times sub appears

names
'HarshithSowmyaKiranVarunMani'
names.count('a') #5
names.count('i') #3
names.count('r') #3

#4.String Testing Methods
