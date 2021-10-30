# Get the positions of each element in a list

List = ['a', 'b', 'c', 'a', 'd', 'a']

# Method 1
print(List.index('a'))
# But in the above method you can only find the single index

# Method 2

Indexes = [i for (i, j) in enumerate(List) if j == 'a']
print(Indexes)
