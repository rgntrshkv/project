from house import House
import random


dr = {0:'Север', 1:'Юг',2:'Восток',3:'Запад'}
hs = House(10,10)
while hs.house[hs.cur_position[0]][hs.cur_position[1]] != 'Балкон':
    dir = random.randint(0,3)
    stp = random.randint(1,3)
    print('Движение на '+dr[dir]+' на '+str(stp)+' шагов')
    hs.move(dir,stp)
