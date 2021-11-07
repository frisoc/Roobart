# https://pythoninwonderland.wordpress.com/2017/03/18/how-to-implement-breadth-first-search-in-python/
from mine import Mine

def bfs_connected_component(graph, start):
    explored = []
    queue = [start]

    while queue:
        node = queue.pop(0)
        if node not in explored:
            explored.append(node)
            neighbours = graph[node]

            for neighbour in neighbours:
                queue.append(neighbour)
    return explored


def bfs_shortest_path(graph, start, goal):
    explored = []
    queue = [[start]]

    if start == goal:
        return "That was easy! Start = goal"

    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node not in explored:
            neighbours = graph[node]
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                if neighbour == goal:
                    return new_path

            explored.append(node)

    return []


# start = [0, 0]
# nodes = {1: [50, 30], 2: [100, 155], 3: [200, 155],
#          4: [305, 110], 5: [110, 280], 6: [340, 275],
#          7: [90, 430], 8: [230, 380], 9: [335, 475]}
# print(bfs_connected_component(list(nodes.values()), start))

graph = {'A': ['B', 'C', 'E'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F', 'G'],
         'D': ['B'],
         'E': ['A', 'B', 'D'],
         'F': ['C'],
         'G': ['C']}
print(bfs_connected_component(graph, "A"))
print(bfs_shortest_path(graph, "A", "G"))

mine_graph = {"A": ["B"],
              "B": ["A", "C", "D"],
              "C": ["B", "D", "G", "H"],
              "D": ["B", "C", "E", "F"],
              "E": ["D"],
              "F": ["F"],
              "G": ["C", "I"],
              "H": ["C"],
              "I": ["G"]
              }
print(bfs_connected_component(mine_graph, "A"))
print(bfs_shortest_path(mine_graph, "A", "G"))

mine_a = Mine("A", 10, 20)
print(type(mine_a))
