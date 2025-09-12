#for append use a,, for append doing another operat^ use a+
try:
    file=open('abc.txt','a')
except FileNotFoundError:
    print("File is not present")
else:
    file.write('Pokemon Master')
    file.close()
finally:
    print("Myself Harshith","\nThe Trainer from Palet town")
