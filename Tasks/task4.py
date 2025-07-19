# Photo gallery

print("Enter photo names you want to share:")
input_photos = input()
photo_list = input_photos.split()
unique_photos = list(set(photo_list))
unique_photos.sort()
print("Photos selected for sharing:")
for photo in unique_photos:
    print(photo)
