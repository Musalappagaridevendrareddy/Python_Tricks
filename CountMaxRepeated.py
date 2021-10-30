# Count max or min repeated value in a list

# Method 1

l = [4, 1, 5, 3, 5, 1, 5]
s = list(set(l))
v = [l.count(c) for c in s]
print(s[v.index(max(v))], ' Repeated ', max(v))
print(s[v.index(min(v))], ' Repeated ', min(v))

# Method 2

print(max(set(l), key=l.count))
print(min(set(l), key=l.count))
