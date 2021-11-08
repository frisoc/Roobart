class Mine:
    def __init__(self, identifier, x, y, neighbors):
        self.identifier = identifier
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

    # def __repr__(self):
    #     return f"Mine: {self.identifier}\n(x, y): {self.x}, {self.y}\nNumber of neighbors: {len(self.neighbors)}"

    def __str__(self):
        return f"Mine: {self.identifier}\n(x, y): {self.x}, {self.y}\nNumber of neighbors: {len(self.neighbors)}"

    def get_num_neighbors(self):
        return len(self.neighbors)
