import math
from mine import Mine
import graph_creation as gc


def calculate_c(a, b):
    """
    Calculates the hypotenuse for a triangle
    :param a: The length of the first leg
    :param b: The length of the second leg
    :return: The length of the hypotenuse
    """
    return math.sqrt((a ** 2) + (b ** 2))


def calculate_dist(p1, p2):
    """
    Calculates the distance between two points (the points are a tuple of (x, y))
    :param p1: The first point (x, y)
    :param p2: The second point (x, y)
    :return: The distance between the two points
    """
    # p1 and p2 are a tuple of x, y
    d = math.sqrt(((p2[1] - p1[1]) ** 2) + ((p2[0] - p1[0]) ** 2))
    return d


def calculate_theta(x, y):
    """
    Calculates the angle in degrees between two legs using tan inverse
    :param x: The length of the leg in the x direction
    :param y: The length of the leg in the y direction
    :return: The angle in degrees
    """
    return math.degrees(math.atan2(y, x))


def find_all_angles(mine_positions):
    """
    Finds all the angles between every point in the path
    :param mine_positions: A dictionary representing the mines and their positions
    :return: A dictionary where the key is the segment ("Vertex1-Vertex2") and the value is the angle in degrees
    """
    ids = list(mine_positions.keys())
    positions = list(mine_positions.values())
    paths = []
    angles = []
    for i in range(len(positions)):
        if i == len(positions) - 1:
            angle = calculate_theta(positions[len(positions) - 1][0] - positions[0][0],
                                    positions[len(positions) - 1][1] - positions[0][1])
            path = f"{ids[len(ids) - 1]}-{ids[0]}"
        else:
            angle = calculate_theta(positions[i + 1][0] - positions[i][0], positions[i + 1][1] - positions[i][1])
            path = f"{ids[i]}-{ids[i + 1]}"
        paths.append(path)
        angles.append(angle)
    return combine_results(paths, angles)


def find_all_distances(mine_positions):
    """
    Finds all the distances between every point in the path
    :param mine_positions: A dictionary representing the mines and their positions
    :return: A dictionary where the key is the segment ("Vertex1-Vertex2") and the value is the distances
    """
    ids = list(mine_positions.keys())
    positions = list(mine_positions.values())
    paths = []
    dists = []
    for i in range(len(positions)):
        if i == len(positions) - 1:
            dist = calculate_dist(positions[len(positions) - 1], positions[0])
            path = f"{ids[len(ids) - 1]}-{ids[0]}"
        else:
            dist = calculate_dist(positions[i + 1], positions[i])
            path = f"{ids[i]}-{ids[i + 1]}"
        paths.append(path)
        dists.append(dist)

    return combine_results(paths, dists)


def combine_results(paths, results):
    """
    Combines the results from the find_all_ functions into a dictionary
    :param paths: The vertex paths in the form of "Vertex1-Vertex2"
    :param results: The calculations from the respective find_all functions
    :return: A dictionary where the key is the vertex path and the value is the respective result
    """
    combo = dict()
    for i in range(len(paths)):
        combo[paths[i]] = results[i]
    return combo


def sort_dict(a_list, a_dict):
    """
    Sorts a dictionary based on a list
    :param a_list: The list to use to sort
    :param a_dict: The unsorted dictionary
    :return: The sorted dictionary
    """
    sorted_dict = dict()
    for ele in a_list:
        sorted_dict[ele] = a_dict[ele]
    return sorted_dict


def assign_mines(raw_pos):
    """
    Takes a list of raw positions of mines and converts it to a dictionary
    :param raw_pos: The list of list coordinates of the mine positions
    :return: A dictionary where the key is the identifier and the value is the list of positions
    """
    complete = {"S": [0, 0]}
    mine_pos = dict()
    for i, pos in enumerate(raw_pos):
        letter = chr(i + 65)
        if letter == "S":
            letter = chr(i + 65 + 1)
        mine_pos[letter] = pos
    complete.update(mine_pos)
    return complete


def create_test_mines1():
    """
    Creates a list of Mine objects for testing
    :return: A list of pre-defined list of Mine objects
    """
    mine_pos = {"S": [0, 0], "A": [10, 15], "B": [14, 27], "C": [20, 27], "D": [20, 17]}

    mine4 = Mine("D", mine_pos["D"][0], mine_pos["D"][1], ["B", "C"])
    mine2 = Mine("B", mine_pos["B"][0], mine_pos["B"][1], ["A", "C", "D"])
    mine3 = Mine("C", mine_pos["C"][0], mine_pos["C"][1], ["B", "D"])
    mine1 = Mine("A", mine_pos["A"][0], mine_pos["A"][1], ["S", "B"])
    mine0 = Mine("S", mine_pos["S"][0], mine_pos["S"][1], ["A"])

    return [mine0, mine1, mine2, mine3, mine4]


def create_test_mines2():
    """
    Creates a list of Mine objects for testing
    :return: A list of pre-defined list of Mine objects
    """
    mine_pos = {"S": [0, 0], "A": [10, 15], "B": [14, 27], "C": [20, 27], "D": [20, 17], "E": [20, 20]}

    mine5 = Mine("E", mine_pos["D"][0], mine_pos["D"][1], ["C", "D"])
    mine4 = Mine("D", mine_pos["D"][0], mine_pos["D"][1], ["B", "C", "E"])
    mine3 = Mine("C", mine_pos["C"][0], mine_pos["C"][1], ["B", "D", "E"])
    mine2 = Mine("B", mine_pos["B"][0], mine_pos["B"][1], ["A", "C", "D"])
    mine1 = Mine("A", mine_pos["A"][0], mine_pos["A"][1], ["S", "B"])
    mine0 = Mine("S", mine_pos["S"][0], mine_pos["S"][1], ["A"])

    return [mine0, mine1, mine2, mine3, mine4, mine5]


def main():
    """
    Main driver
    :return: None
    """
    coords = [[0, 10], [15, 20], [30, 10]]
    mine_pos = assign_mines(coords)
    graph, path = gc.find_path("S", mine_pos)

    sorted_dict = sort_dict(path, mine_pos)
    angles = find_all_angles(sorted_dict)
    dists = find_all_distances(sorted_dict)

    print(graph, path)
    print(angles)
    print(dists)


def testing():
    # mine_pos = {"S": [0, 0], "A": [10, 15], "B": [14, 27], "C": [20, 27], "D": [20, 17]}
    # mines = create_test_mines1()

    mine_pos = {"S": [0, 0], "A": [10, 15], "B": [14, 27], "C": [20, 27], "D": [20, 17], "E": [20, 20]}
    mines = create_test_mines2()

    mine_graph = gc.make_graph(mines)
    path = gc.bfs_connected_component("S", mine_graph)
    print(mine_graph, "\n", path)
    print(find_all_angles(mine_pos))
    print(find_all_distances(mine_pos))

    graph, path = gc.find_path("S", mine_pos)
    print(graph, path)

    a = sort_dict(path, mine_pos)
    print(find_all_angles(a))
    print(find_all_distances(a))


if __name__ == '__main__':
    main()
