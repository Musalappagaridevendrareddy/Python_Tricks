# Sort list in a single line

l = [4, 2, 1, 3]

list1 = [l.pop(l.index(min(l))) for i in range(len(l))]
print(list1)

l2 = [1, 8, 4, 5]
print(sorted(l2))
