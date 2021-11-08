"""
Author: Chris Botzoc and Nikhil Gajghate
Date Due: 10/25/2021
Class: Robotics
Instructor: Velez
"""
from mine import Mine
from random import randint


def bfs_connected_component(start, graph):
    """
    Implementation of breadth-first search to search through a set of points
    :param start: The starting position of the robot
    :param graph: The list of points to build a path from
    :return: The path of the graph
    """
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


def bfs_shortest_path(start, goal, graph):
    """
    Implementation of breadth-first search to find the shortest path through a set of points
    :param start: The starting position of the robot
    :param goal: The goal position
    :param graph: The list of points to build a path from
    :return: The shortest path of the graph from start to goal
    """
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


def create_mines(nodes):
    """
    Creates a list of Mine objects from a list of positions
    :param nodes: A list of positions where the positions are a list of [y, x]
    :return: A list of Mine objects
    """
    mines = []
    for k, v in nodes.items():
        mine = Mine(k, v[0], v[1], [])
        mines.append(mine)

    return mines


def create_neighbors(mines):
    """
    Randomly assigns neighbors to a list of Mines
    :param mines: A list of Mine objects
    :return: None
    """
    for mine in mines:
        num_mines = randint(1, 3)
        for i in range(num_mines):
            mine_select = randint(0, len(mines) - 1)
            while mines[mine_select] not in mine.neighbors:
                mine.add_neighbor(mines[mine_select])
                mine_select = randint(0, len(mines) - 1)


def make_graph(mines):
    """
    Builds a graph
    :param mines:
    :return:
    """
    mine_graph = dict()
    for mine in mines:
        neighbor_list = []
        for neighbor in mine.neighbors:
            neighbor_list.append(neighbor.identifier)
        mine_graph[mine.identifier] = neighbor_list

    return mine_graph


def find_path(start, mine_positions):
    """
    Finds a path from a start position and generates a graph from a dictionary of positions
    :param start: A key from the mine_positions dictionary to start the path from
    :param mine_positions: A dictionary of a mine identifier as the key with their [x, y] position as the value
    :return: The graph that was generated and the BFS path
    """
    mines = create_mines(mine_positions)
    create_neighbors(mines)
    mine_graph = make_graph(mines)

    path = bfs_connected_component(start, mine_graph)
    return mine_graph, path


def main():
    """
    Main driver
    :return: None
    """
    mine_pos_2 = dict()

    mine_pos = {1: [50, 30], 2: [100, 155], 3: [200, 155],
                4: [305, 110], 5: [110, 280], 6: [340, 275],
                7: [90, 430], 8: [230, 380], 9: [335, 475]}

    for k, v in mine_pos.items():
        mine_pos_2[chr(k + 64)] = v

    graph1, path1 = find_path(1, mine_pos)
    graph2, path2 = find_path("D", mine_pos_2)

    print(graph1, path1)
    print(graph2, path2)


if __name__ == '__main__':
    main()
