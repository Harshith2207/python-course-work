#7.2 Dictionary Execution

#Syntax of Dictionary
''' dict_name={key1: value1, key2: value2, key3: value3} '''

student = {
"name": "Harshith",
"id": 123,
"course": "Cyber Security"
}
print(student) #{'name': 'Harshith', 'id': 123, 'course': 'Cyber Security'}

#Accessing values

print(student["name"]) #Output: Harshith
print(student.get("id")) # Output: 123
print(student.get("city", "Not Available")) # Output: Not Available

#Adding & Updating Items

student["id"] = 456 # Updating existing key
student["city"] = "New York" # Adding a new key-value pair
print(student) #{'name': 'Harshith', 'id': 456, 'course': 'Cyber Security', 'city': 'New York'}

#Removing Items

id = student.pop("id")
print(id) # Output: 456
print(student) #{'name': 'Harshith', 'course': 'Cyber Security', 'city': 'New York'}

del student["course"]
print(student)  #{'name': 'Harshith', 'city': 'New York'}

student.popitem()
print(student)  #{'name': 'Harshith'}

student.clear()
print(student) #Output: {}

