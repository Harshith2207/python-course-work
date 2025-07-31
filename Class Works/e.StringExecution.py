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
#startswith(sub)

'PFS15'.startswith('DS') #False
'JFS15'.startswith('DS') #False
'DS15'.startswith('DS') #True
l=['PFS14','DS-11','DA-14','PFS-15','JS-12','DS-15','DS-14']
for i in l:
    if i.startswith('DS'):
        print(i) #DS-11 DS-15 DS-14

#endswith(sub)

l=['hello.py','demo.png','resume.pdf','oper.py','python.py']
for i in l:
    if i.endswith('.py'):
        print(i) #hello.py oper.py python.py

#isalpha()

s='sowmya'
s.isalpha() #True
s='varun123'
s.isalpha() #False

#isalnum()

s.isalnum() #True

#islower()

s.islower() #True

#isupper()

s.isupper() #False

#isspace

s.isspace() #False
' '.isspace() #True
'     '.isspace() #True

#isidentifier()

'@myvae'.isidentifier() #False
'my_var'.isidentifier() #True

#isdigit()

'١٢٣'.isdigit() #True
'123'.isdigit() #True
'⓫'.isdigit() #False
'۵'.isdigit() #True

#isnumeric()

'五'.isnumeric() #True

#5.Replace & Modify Methods
#replace(old,new)

s='Tatik'
s.replace('i','ee') #'Tateek'
s='python pgrm lang'
s.replace(' ','') #'pythonpgrmlang'
s #'python pgrm lang'

#maketrans()

pwd='harshith@123'
pwd.translate(str.maketrans("a13h", "@o#8")) #'8@rs8it8@o2#'
pwd.translate(str.maketrans("@o#8", "a13h")) #'harshitha123'
"harshit".maketrans("a13h", "@o#8") #{97: 64, 49: 111, 51: 35, 104: 56}
pwd.maketrans("a13h", "@o#8") #{97: 64, 49: 111, 51: 35, 104: 56}

#6.Splitting & Joining Methods
#split(sep)

s='My name is Tarit'
s.split() #['My', 'name', 'is', 'Tarit']
s.split('a') #['My n', 'me is T', 'rit']
i='Varun,Harshith,Hemanth'
i.split(',') #['Varun', 'Harshith', 'Hemanth']
s #'My name is Tarit'
s.split() #['My', 'name', 'is', 'Tarit']

#rsplit(sep)

s.rsplit(' ',2) #['My name', 'is', 'Tarit']

#splitlines()

file='''Hello
world
python
program
'''
file #'Hello\nworld\npython\nprogram\n'
file.splitlines() #['Hello', 'world', 'python', 'program']

#join(iterable)

file=['Hello', 'world', 'python', 'program']
''.join(file) #'Helloworldpythonprogram'
' '.join(file) #'Hello world python program'
'@'.join(file) #'Hello@world@python@program'
','.join(file) #'Hello,world,python,program'

#partition(sep)

'pythonprgm.py'.partition('.') #('pythonprgm', '.', 'py')

#rpartition(sep)

'pythonprgm.file.py'.rpartition('.') #('pythonprgm.file', '.', 'py')
'1.pythonprgm.py'.rpartition('.') #('1.pythonprgm', '.', 'py')



file #['Hello', 'world', 'python', 'program']
file='''Hello
world
python
program
'''
file.split('\n') #['Hello', 'world', 'python', 'program', '']

#7.Whitespace & Trimming Methods
#strip(chars)

s='           python          '
s.strip() #'python'

#lstrip(chars)

s.lstrip() #'python          '

#rstrip(chars)

s.rstrip() #'           python'
s #'           python          '

#8.Encoding & Decoding Methods
#encode(encoding)-Converts string to bytes
#decode(decoding)-Converts bytes back to string

s.encode() #b'           python          '
text = "Hello 🙂"
text.encode() #b'Hello \xf0\x9f\x99\x82'

b'Hello \xf0\x9f\x99\x82'.decode() #'Hello 🙂'

text="नमते你好"
text.encode() #b'\xe0\xa4\xa8\xe0\xa4\xae\xe0\xa4\xa4\xe0\xa5\x87\xe4\xbd\xa0\xe5\xa5\xbd'

b'\xe0\xa4\xa8\xe0\xa4\xae\xe0\xa4\xa4\xe0\xa5\x87\xe4\xbd\xa0\xe5\xa5\xbd'.decode() #'नमते你好'

'banana'.count('na') #2
'abcbcbc'.count('cbc') #1

'tarit'.maketrans('a','@') #{97: 64}
'tarit'.translate('tarit'.maketrans('a','@')) #'t@rit'
'tarit'.translate(str.maketrans('a','@')) #'t@rit'
