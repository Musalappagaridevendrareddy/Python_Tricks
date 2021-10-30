# Convert nested list into list in a single line

# Method 1

List = [[1, 2], [3, 4], [5, 6]]
Converted_list = [y for x in List for y in x]
print(Converted_list)

# Method 2 

import itertools
comList = list(itertools.chain.from_iterable(List))
print(comList)
