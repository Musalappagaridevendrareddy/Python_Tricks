#  Find all the indexes of a pattern(Sub string) in a string

# # Method 1
import re

string = "Hello World, this is devendar welcome to my channel"
pattern = "is"
a = 0
List = []
for i in range(len(string)):
    a = a + len(pattern)
    try:
        List.append(string.index(pattern, a, len(string)))
    except:
        pass
print(List)

# # Method 2

print([i for i in range(len(string)) if string.startswith(pattern, i)])

# # Method 3

print([m.start() for m in re.finditer(pattern, string)])
