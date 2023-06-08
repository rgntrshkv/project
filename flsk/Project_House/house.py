import random
import pandas as pds
from threading import Lock
import copy as cp


class SingletonMeta(type):
    _instances = {}
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances or args or kwargs:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]

class House(metaclass=SingletonMeta):

    room_names = ['Коридор', 'Кухня', 'Ванная','Холл','Спальня','Столовая','Кладовка','Библиотека','Детская','Кабинет','Гардеробная','Аквадискотека','Комната грязи']

    def __init__(self, width=3, height=2):
        self.__width = width
        self.__height = height
        self.cur_position = [0,0]
        self.house = self.generate_house()
        
    def generate_house(self):
        rn = self.room_names.copy()
        room_house = [[random.randint(0, 1) for _ in range(self.__width)] for _ in range(self.__height)]
        n = 0
        for i in range(self.__height):
            for j in range(self.__width):
                if i==0 and j==0:
                    room_house[i][j] = 'Подземелье'
                elif rn == []:
                    room_house[i][j] = 'Гостевая'+str(n)
                    n+=1
                else:
                    el = random.choice(rn)
                    room_house[i][j] = el
                    rn.remove(el)
        room_house[self.__height-1][random.randint(0,self.__width-1)] = 'Балкон'
        print(room_house)
        room = room_house[self.cur_position[0]][self.cur_position[1]]
        msg = "Вы находитесь в комнате "+room 
        print(msg)
        return room_house
    
    def one_step(self, direction):
        dr = direction
        if dr == 0:
            if self.cur_position[0]+1 > self.__height-1:
                status = 0
            else:
                self.cur_position[0]+=1
                status = 1
        if dr == 1:
            if self.cur_position[0]-1 < 0:
                status = 0
            else:
                self.cur_position[0]+=-1
                status = 1  
        if dr == 2:
            if self.cur_position[1]+1 > self.__width-1:
                status = 0
            else:
                self.cur_position[1]+=1
                status = 1
        if dr == 3:
            if self.cur_position[1]-1 < 0:
                status = 0
            else:
                self.cur_position[1]+=-1
                status = 1  
        return status

    def move(self, direction, count_steps):
        msg = ''
        for s in range(count_steps):
            status = self.one_step(direction)
            if status == 0:
                msg = msg+"Вы не можете дальше пройти"
                #print(msg)
                break
            else:
                room = self.house[self.cur_position[0]][self.cur_position[1]]
                if room == 'Балкон':
                    msg = msg+"Вы находитесь на Балконе. Поздравляю, это Вин!"
                    #print(msg)
                    break
                else:
                    msg = msg+"Вы находитесь в комнате "+room+" -> "
                    #print(msg)
        return msg

    @staticmethod
    def __get_near(universe, pos, system=None):
        if system is None:
            system = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))

        count = 0
        for i in system:
            if universe[(pos[0] + i[0]) % len(universe)][(pos[1] + i[1]) % len(universe[0])]:
                count += 1
        return count