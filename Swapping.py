# Swapping variables in a single line

a = 10
b = 20
print(f"a={a}, b = {b} Before change")
a, b = b, a

print(f'a={a}, b={b} after swapping')
