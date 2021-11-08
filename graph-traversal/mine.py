class Mine:
    def __init__(self, letter, x, y, neighbors):
        self.letter = letter
        self.x = x
        self.y = y
        self.neighbors = neighbors

    def add_neighbor(self, neighbor):
        if type(neighbor) == Mine:
            self.neighbors.append(neighbor)
        elif type(neighbor) == list:
            self.neighbors += neighbor

    def get_y_x(self):
        return [self.y, self.x]
