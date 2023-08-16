from liczby_2 import find_max
from liczby_3 import find_min

numbers =[int(x) for x in input().split()]                   

max = find_max(numbers)
min = find_min(numbers)

print("max number is", max, "and min number is", min)

