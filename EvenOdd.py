# Even or odd in single line

a = 5

evenOROdd = "Even" if a % 5 == 0 else "Odd"
print(evenOROdd)

EO = lambda x: True if x % 2 == 0 else False

print(EO(10))
