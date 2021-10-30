# Sort list in a single line

# Method 1

l = [4, 2, 1, 3]

list1 = [l.pop(l.index(min(l))) for i in range(len(l))]
print(list1)

# Method 2

l2 = [1, 8, 4, 5]
print(sorted(l2))
