class Matrix:

    def __init__(self):
        self.counter = 0
        self.matrix = [
            [None, 'Балкон', None],
            ['Спальня', 'Холл', 'Кухня'],
            ['Подземелье', 'Коридор', 'Оружейная']
        ]
        self.location = 'Подземелье'

    def movement(self, path: int, step: int):
        index_i = ''
        index_j = ''
        flag = True
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] == self.location:
                    index_i = i
                    index_j = j
        if path == 1:
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[i])):
                    if i == index_i and j == index_j + step and self.matrix[i][j] is not None:
                        self.location = self.matrix[i][j]
                        return self.location, flag
            else:
                for i in range(len(self.matrix)):
                    for j in range(len(self.matrix[i])):
                        if i == index_i:
                            self.location = self.matrix[i][2]
                            flag = False
                            return self.location, flag
        elif path == 3:
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[i])):
                    if i == index_i and j == index_j - step and self.matrix[i][j] is not None:
                        self.location = self.matrix[i][j]
                        return self.location, flag
            else:
                for i in range(len(self.matrix)):
                    for j in range(len(self.matrix[i])):
                        if i == index_i:
                            self.location = self.matrix[i][0]
                            flag = False
                            return self.location, flag
        elif path == 0:
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[i])):
                    if i == index_i - step and j == index_j and self.matrix[i][j] is not None:
                        self.location = self.matrix[i][j]
                        return self.location, flag
            else:
                for i in range(len(self.matrix)):
                    for j in range(len(self.matrix[i])):
                        if j == index_j and index_j not in (0, 2):
                            self.location = self.matrix[0][j]
                            flag = False
                            return self.location, flag
                else:
                    for i in range(len(self.matrix)):
                        for j in range(len(self.matrix[i])):
                            if j == index_j:
                                self.location = self.matrix[1][j]
                                flag = False
                                return self.location, flag
        elif path == 2:
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[i])):
                    if i == index_i + step and j == index_j:
                        if self.matrix[i][j] is not None:
                            self.location = self.matrix[i][j]
                            return self.location, flag
            else:
                for i in range(len(self.matrix)):
                    for j in range(len(self.matrix[i])):
                        if j == index_j:
                            self.location = self.matrix[2][j]
                            flag = False
                            return self.location, flag
