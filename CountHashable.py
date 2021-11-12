# Count hashable objects with collections

from collections import Counter

List = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 1]
counter = Counter(List)  # This stores the count of each item in the list

print(counter)

Most_common = counter.most_common(2)  # This returns the most common item in the list
print(Most_common)

# To find the second most common element in the list just replace 1 with any other element
# You will get the list of common elements in the list
# To get the only the first one use [0]
print(Most_common[1][0])
