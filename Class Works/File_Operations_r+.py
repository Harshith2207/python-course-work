with open('abc.txt','r+') as file:
    file.write('\nFile Operations')
    file.seek(0)
    print(file.read())
