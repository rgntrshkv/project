import random as rnd
import statistics as st

numbers = []
ncnt = rnd.randint(10,20)

for n in range(ncnt):
    numbers.append(rnd.randint(0,100))
numbers.sort()
hcnt = ncnt//2
if ncnt%2 == 1:
    medn = numbers[hcnt]
else:
    medn = (numbers[hcnt-1]+numbers[hcnt])/2
    
print(ncnt)
print(numbers)
print(medn)
print(st.median(numbers))

