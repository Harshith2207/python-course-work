try:
    file=open('Conditional Statements.txt','r')
except FileNotFoundError:
    print("File is not present")
else:
    read=file.read()
    file.seek(0)
    readlines=file.readlines()
    file.seek(0)
    readline=file.readline()
    print(f"\nFile Content using read(): \n{read}")
    print(f"\nFile Content using readlines(): \n{readlines}")
    print(f"\nFile Content using readline(): \n{readline}")
    file.close()
