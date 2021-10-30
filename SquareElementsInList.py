# Square elements in a list with in a single line

l = [1, 2, 3, 4, 5, 6, 7, 8]

square = list(map(lambda x: x ** 2, l))
print(square)

cube = list(map(lambda x: x ** 3, l))
print(cube)
