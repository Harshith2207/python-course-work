# Photo gallery

names={'Sun':1,'Moon':2,'Star':3,'Earth':4,'Mercury':5,'Venus':6,'Mars':7,'Neptune':8,'Jupyter':9}
print("Enter photo {names} you want to share:")
photos=input()
plist=photos.split()
unique_photos=list(set(plist))
unique_photos.sort()
print("Selected photos for sharing: ")
for photo in unique_photos:
    print(photo)
print(names)