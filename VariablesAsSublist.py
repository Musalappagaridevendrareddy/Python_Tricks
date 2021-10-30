# Assigning the elements in a list to variables

a, b, *c = [1, 2, 3, 4, 5, 6]
print(a, b, c)

d, e, *_ = (1, 2, 3, 4, 5, 6)
print(d, e)

a1, b1, *c1, d1 = (1, 2, 3, 4, 5)
print(a1, b1, c1, d1)

x, *y, z = (1, 2, 5, 4, 7)
print(x, y, z)
