# """
# Author: Chris Botzoc and Nikhil Gajghate
# Date Due: 10/25/2021
# Class: Robotics
# Instructor: Velez
# """
# import cv2 as cv
# import numpy as np
# from math import sqrt
# from mine import Mine
# from random import randint
# from random import choices
#
# callBackImg = None
#
#
# def printRGB(event, x, y, flags, params):
#     (height, width, channels) = callBackImg.shape
#     # EVENT_MOUSEMOVE
#     if event == cv.EVENT_LBUTTONDOWN:
#         if channels == 3:
#             print(str(x) + " " + str(y) + " " + str(callBackImg[y][x][2]) + " " + str(callBackImg[y][x][1]) + " " + str(
#                 callBackImg[y][x][0]))
#         else:
#             print("x: " + str(x) + " " + "y: " + str(y) + " " + "color: " + str(callBackImg[y][x][0]))
#
#
# def showImage(images):
#     global callBackImg
#     for i in range(len(images)):
#         if i == 0:
#             callBackImg = images[i]
#         cv.imshow("Image " + str(i), images[i])
#         cv.setMouseCallback("Image " + str(i), printRGB)
#     while True:
#         k = cv.waitKey(0)
#         if k == ord("q"):
#             break
#     cv.destroyAllWindows()
#
#
# def bfs_connected_component(start, graph):
#     """
#     Implementation of breadth-first search to search through a set of points
#     :param start: The starting position of the robot
#     :param graph: The list of points to build a path from
#     :return: The path of the graph
#     """
#     explored = []
#     queue = [start]
#
#     while queue:
#         node = queue.pop(0)
#         if node not in explored:
#             explored.append(node)
#             neighbours = graph[node]
#
#             for neighbour in neighbours:
#                 queue.append(neighbour)
#     return explored
#
#
# def bfs_shortest_path(start, goal, graph):
#     """
#     Implementation of breadth-first search to find the shortest path through a set of points
#     :param start: The starting position of the robot
#     :param goal: The goal position
#     :param graph: The list of points to build a path from
#     :return: The shortest path of the graph from start to goal
#     """
#     explored = []
#     queue = [[start]]
#
#     if start == goal:
#         return "That was easy! Start = goal"
#
#     while queue:
#         path = queue.pop(0)
#         node = path[-1]
#         if node not in explored:
#             neighbours = graph[node]
#             for neighbour in neighbours:
#                 new_path = list(path)
#                 new_path.append(neighbour)
#                 queue.append(new_path)
#                 if neighbour == goal:
#                     return new_path
#
#             explored.append(node)
#
#     return []
#
#
# def findBlob(orig, color):
#     """
#     Segments an image using OpenCV
#     :param orig: The original image to segment
#     :param color: The color to segment for
#     :return: The segmented image
#     """
#     (height, width, channels) = orig.shape
#     lower_range = color - 1
#     upper_range = color + 1
#     mask = cv.inRange(orig, lower_range, upper_range)
#     mask = mask.reshape(height, width, 1)
#     return mask
#
#
# def drawPath(img, path):
#     """
#     Draws a path generated from A*
#     :param img: The image to draw on
#     :param path: A list of coordinates
#     :return: None
#     """
#     for p in path:
#         cv.line(img, (p[1], p[0]), 0, 1)
#
#
# def draw_centroid(image):
#     """
#     Draws a centroid on a segmented image by taking the mean of all the white pixels
#     :param image: The segmented image to draw a centroid on
#     :return: None
#     """
#     x_coords = np.nonzero(image)[0]
#     y_coords = np.nonzero(image)[1]
#
#     x_center = np.round(np.mean(x_coords))
#     y_center = np.round(np.mean(y_coords))
#
#     return int(x_center), int(y_center)
#
#
# def create_mines(nodes):
#     """
#     Creates a list of Mine objects from a list of positions
#     :param nodes: A list of positions where the positions are a list of [y, x]
#     :return: A list of Mine objects
#     """
#     mines = []
#     for k, v in nodes.items():
#         mine = Mine(k, v[1], v[0], [])
#         mines.append(mine)
#
#     return mines
#
#
# def add_neighbors(mines):
#     """
#     Randomly assigns neighbors to a list of Mines
#     :param mines: A list of Mine objects
#     :return: None
#     """
#     for mine in mines:
#         num_mines = randint(1, 3)
#         for i in range(num_mines):
#             mine_select = randint(0, len(mines) - 1)
#             while mines[mine_select] not in mine.neighbors:
#                 mine.add_neighbor(mines[mine_select])
#                 mine_select = randint(0, len(mines) - 1)
#
#
#
# def readIMG():
#     global callBackImg
#     cv.samples.addSamplesDataSearchPath(
#         "/graph-traversal/")
#     orig = cv.imread(cv.samples.findFile("minefield.jpg"))
#     # orig = cv.imread("/graph-traversal/minefield-colored.png.jpg")
#     # print(orig)
#     callBackImg = orig
#     cv.imshow("Display window", orig)
#     while True:
#         k = cv.waitKey(1)
#         cv.setMouseCallback('Display window', printRGB)
#         if k == ord('s'):
#             cv.imwrite('testSave.png', callBackImg)
#         elif k == ord('q'):
#             break
#
#
# def main():
#     """
#     Main driver
#     :return: None
#     """
#     # scale = 10
#     #
#     # (img, path) = path_minefield()
#     #
#     # (height, width, channels) = img.shape
#     # scale = 10
#     # resize = cv.resize(img, (width * scale, height * scale))
#     # (height, width) = resize.shape
#     # resize = resize.reshape(height, width, 1)
#     # rPath = []
#     #
#     # for p in path:
#     #     rPath.append([p[0] * scale, p[1] * scale])
#     #
#     # print("Path", rPath)
#     #
#     # drawPath(resize, rPath)
#     # showImage([resize])
#     # readIMG()
#     # path_minefield
#     nodes = {1: [50, 30], 2: [100, 155], 3: [200, 155],
#              4: [305, 110], 5: [110, 280], 6: [340, 275],
#              7: [90, 430], 8: [230, 380], 9: [335, 475]}
#     mines = create_mines(nodes)
#     # print(mines)
#     add_neighbors(mines)
#     print(mines[0])
#     mine_graph = dict()
#     for mine in mines:
#         neighbor_list = []
#         for neighbor in mine.neighbors:
#             neighbor_list.append(neighbor.identifier)
#         mine_graph[mine.identifier] = neighbor_list
#     print(mine_graph)
#     print(len(bfs_connected_component(1, mine_graph)))
#
#
# if __name__ == '__main__':
#     main()
