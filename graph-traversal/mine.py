class Mine:
    def __init__(self, letter, x, y):
        self.letter = letter
        self.x = x
        self.y = y
        self.neighbors = []

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)