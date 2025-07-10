#2. if-else Statement

#Doraemon Gadeget Store

gadgets=['Anywhere door','small light','big light','magic pencil','helicopter','toycar']

print('Hey User Welcome to the Doraemon Store'.center(50,'-'))
searchinput=input("Enter the gadgets:").lower()

if searchinput in gadgets:
    print(f"{searchinput} found. Buy now!!!")
else:
    print(f'{searchinput} is in repair now. Come later...')
