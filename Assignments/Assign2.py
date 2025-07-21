chat = {}
n = int(input("Enter number of messages: "))
for i in range(n):
    name = input("Name: ")
    msg = input("Message: ")
    if name and msg:
        chat[i+1] = {'name': name, 'msg': msg}
for k in chat: print(f"{chat[k]['name']}: {chat[k]['msg']}")
