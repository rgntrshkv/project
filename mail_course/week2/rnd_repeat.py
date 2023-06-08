import random as rnd
rnd_set = set()
iter_num = 0
while True:
    iter_num += 1
    rnd_n = rnd.randint(0,1000)
    if rnd_n in rnd_set:
        break
    else:
        rnd_set.add(rnd_n)

print(rnd_set)
print(rnd_n)
print(iter_num)