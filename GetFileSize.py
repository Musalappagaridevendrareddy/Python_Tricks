# Get file size in different formats

import os

info = os.stat('tricks.py')
print(info.st_size, '-bytes\n', info.st_size / 1000, '-KB\n', info.st_size / 1e+6, '-MB')
