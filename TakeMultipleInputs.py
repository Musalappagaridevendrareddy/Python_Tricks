# Taking multiple inputs in a single line

# Method 1

Input = input().split()

print(f'Out1={Input[0]}, Out2={Input[1]}')

# Method 2
a, b = input().split()

print(f'a={a}, b={b}')
