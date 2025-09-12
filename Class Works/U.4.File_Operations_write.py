#for write use w,, for append doing another operat^ use w+
try:
    file=open('abc.txt','w')
except FileNotFoundError:
    print("File is not present")
else:
    file.write('Pokemon Master')
    file.close()
finally:
    print("Myself Harshith","\nThe Trainer from Palet town")
