
import sys

ascending = [1, 2, 3, 4, 5, 6, 7, 8]
descending = [8, 7, 6, 5, 4, 3, 2, 1]
a, b, c, d, e, f, g, h = map(int, input().split())
list = [a, b, c, d, e, f, g, h ]

if ascending == list:
  print("ascending")
elif descending == list:
  print("descending")
else:
  print("mixed")
