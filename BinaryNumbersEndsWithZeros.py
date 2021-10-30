# Find if binary numbers ends with Zeros

N = 5
for i in range(16):
	b = bin(i)[2:].zfill(N)
	if len(b) == N:
		if b.endswith('000'):
			print(b, "->Ends with 000")
		else:
			print(b, "->Does not ends with 000")
