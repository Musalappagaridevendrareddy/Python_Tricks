# Separate characters and numbers from a string
import re

String = '3 apples, 5 bananas, 6 oranges'

Numbers = re.findall(r'(\d+)', String)
Words = re.findall(r'[a-zA-Z]+', String)

print(Numbers, Words)
