#  Fibonacci series in a single line

n = int(input("Enter the range:"))
a, b, sum, count = 0, 1, 0, 1
print("Fibonacci series:", end='')
while (count <= n):
	print(sum, end=" ")
	count += 1
	a = b
	b = sum
	sum = a + b

#  Method 2
print()
fib = lambda x: x if x <= 1 else fib(x - 1) + fib(x - 2)
print("Fibonacci series:", end="")
for i in range(n):
	print(fib(i), end=' ')
