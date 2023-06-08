from abc import ABC, abstractmethod


class Room(ABC):
    def __init__(self, way, number_steps):
        self.points_of_view = [
            (0, 'север'),
            (1, 'восток'),
            (2, 'юг'),
            (3, 'запад')
        ]
        self.message = ""
        self.way = way
        self.number_steps = number_steps

    @abstractmethod
    def validate(self):
        pass


class Dungeon(Room):
    message = "Вы находитесь в подземелье"

    def __init__(self, way, number_steps):
        super().__init__(way, number_steps)

    def validate(self):
        if self.way == 0:
            if self.number_steps == 1:
                return Bedroom
            elif self.number_steps == 2:
                return "error"
        elif self.way == 1:
            if self.number_steps == 1:
                return Hallway
            elif self.number_steps == 2:
                return Armoury
        elif self.way == 2:
            return "error"
        elif self.way == 3:
            return "error"


class Hallway(Room):
    message = "Вы находитесь в коридоре"

    def __init__(self, way, number_steps):
        super().__init__(way, number_steps)

    def validate(self):
        if self.way == 0:
            if self.number_steps == 1:
                return Hall
            elif self.number_steps == 2:
                return "win"
        elif self.way == 1:
            if self.number_steps == 1:
                return Armoury
            elif self.number_steps == 2:
                return "error"
        elif self.way == 2:
            return "error"
        elif self.way == 3:
            if self.number_steps == 1:
                return Dungeon
            elif self.number_steps == 2:
                return "error"


class Armoury(Room):
    message = "Вы находитесь в оружейной"

    def __init__(self, way, number_steps):
        super().__init__(way, number_steps)

    def validate(self):
        if self.way == 0:
            if self.number_steps == 1:
                return Kitchen
            elif self.number_steps == 2:
                return "error"
        elif self.way == 1:
            return "error"
        elif self.way == 2:
            return "error"
        elif self.way == 3:
            if self.number_steps == 1:
                return Hallway
            elif self.number_steps == 2:
                return Dungeon


class Bedroom(Room):
    message = "Вы находитесь в спальне"

    def __init__(self, way, number_steps):
        super().__init__(way, number_steps)

    def validate(self):
        if self.way == 0:
            return "error"
        elif self.way == 1:
            if self.number_steps == 1:
                return Hall
            elif self.number_steps == 2:
                return Kitchen
        elif self.way == 2:
            if self.number_steps == 1:
                return Dungeon
            elif self.number_steps == 2:
                return "error"
        elif self.way == 3:
            return "error"


class Hall(Room):
    message = "Вы находитесь в холле"

    def __init__(self, way, number_steps):
        super().__init__(way, number_steps)

    def validate(self):
        if self.number_steps == 2:
            return "error"
        elif self.way == 0:
            return "win"
        elif self.way == 1:
            return Kitchen
        elif self.way == 2:
            return Hallway
        elif self.way == 3:
            return Bedroom


class Kitchen(Room):
    message = "Вы находитесь на кухне"

    def __init__(self, way, number_steps):
        super().__init__(way, number_steps)

    def validate(self):
        if self.way == 0 or self.way == 1:
            return "error"
        elif self.way == 2:
            if self.number_steps == 1:
                return Armoury
            elif self.number_steps == 2:
                return "error"
        elif self.way == 3:
            if self.number_steps == 1:
                return Hall
            elif self.number_steps == 2:
                return Bedroom
