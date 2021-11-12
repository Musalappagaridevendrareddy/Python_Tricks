# Get and setdefault methods in python

Dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First', 'Count': 15}
Count = Dict.get('Name', 'Not found')  # This code Returns Not found if the key is not found

print(Count)

Count1 = Dict.setdefault('Count', 5)  # This code Returns 5 if the key is not found and Set's the value of the key
print(Count1)

