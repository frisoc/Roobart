"""
Author: Chris Botzoc and Nikhil Gajghate
Date Due: 10/25/2021
Class: Robotics
Instructor: Velez
"""
import cv2 as cv
import numpy as np
from math import sqrt

callBackImg = None


def printRGB(event, x, y, flags, params):
    (height, width, channels) = callBackImg.shape
    # EVENT_MOUSEMOVE
    if event == cv.EVENT_LBUTTONDOWN:
        if channels == 3:
            print(str(x) + " " + str(y) + " " + str(callBackImg[y][x][2]) + " " + str(callBackImg[y][x][1]) + " " + str(
                callBackImg[y][x][0]))
        else:
            print("x: " + str(x) + " " + "y: " + str(y) + " " + "color: " + str(callBackImg[y][x][0]))


def showImage(images):
    global callBackImg
    for i in range(len(images)):
        if i == 0:
            callBackImg = images[i]
        cv.imshow("Image " + str(i), images[i])
        cv.setMouseCallback("Image " + str(i), printRGB)
    while True:
        k = cv.waitKey(0)
        if k == ord("q"):
            break
    cv.destroyAllWindows()


def getNeighbors_(img, point):
    """
    Find the neighboring points within an image
    :param img: The image to find the neighbors in
    :param point: The point in the image
    :return: A list of the valid neighbors
    """
    neighbors = []
    y = point[0]
    x = point[1]
    (height, width, channels) = img.shape
    for i in range(4):
        new_point = []
        new_y_pos = 0
        new_x_pos = 0
        if i == 0:
            new_y_pos = y + 1
            new_x_pos = x
        elif i == 1:
            new_x_pos = x + 1
            new_y_pos = y
        elif i == 2:
            new_y_pos = y - 1
            new_x_pos = x
        elif i == 3:
            new_x_pos = x - 1
            new_y_pos = y

        if (new_x_pos >= width or new_y_pos >= height) or (new_x_pos <= 0 or new_y_pos <= 0):
            new_color = 255
        else:
            new_color = img[new_y_pos][new_x_pos]
            new_point = [new_y_pos, new_x_pos]

        if new_color != 255:
            neighbors.append(new_point)

    return neighbors


def dist(p1, p2):
    """
    Calculates the distance between two points (the points are a tuple of (y, x))
    :param p1: The first point (y, x)
    :param p2: The second point (y, x)
    :return: The distance between the two points
    """
    # p1 and p2 are a tuple of y, x
    d = sqrt(((p2[1] - p1[1]) ** 2) + ((p2[0] - p2[0]) ** 2))
    return d


def bfs(start, nodes):
    visited = list()
    queue = list()
    visited.append(start)
    queue.append(start)
    while queue:
        s = queue.pop(0)
        for n in nodes:
            if n not in visited:
                visited.append(n)
                queue.append(n)
    return visited, queue


def findBlob(orig, color):
    """
    Segments an image using OpenCV
    :param orig: The original image to segment
    :param color: The color to segment for
    :return: The segmented image
    """
    (height, width, channels) = orig.shape
    lower_range = color - 1
    upper_range = color + 1
    mask = cv.inRange(orig, lower_range, upper_range)
    mask = mask.reshape(height, width, 1)
    return mask


# def drawPath(img, path):
#     """
#     Draws a path generated from A*
#     :param img: The image to draw on
#     :param path: A list of coordinates
#     :return: None
#     """
#     for p in path:
#         cv.circle(img, (p[1], p[0]), 5, (125), -1)

def drawPath(img, path):
    """
    Draws a path generated from A*
    :param img: The image to draw on
    :param path: A list of coordinates
    :return: None
    """
    for p in path:
        cv.line(img, (p[1], p[0]), 0, 1)


def draw_centroid(image):
    """
    Draws a centroid on a segmented image by taking the mean of all the white pixels
    :param image: The segmented image to draw a centroid on
    :return: None
    """
    x_coords = np.nonzero(image)[0]
    y_coords = np.nonzero(image)[1]

    x_center = np.round(np.mean(x_coords))
    y_center = np.round(np.mean(y_coords))

    return int(x_center), int(y_center)

def path_minefield():
    """
    Runs the A* implementation on the image for Task 2
    :return: The image and path list
    """
    file_str = "minefield.jpg"
    nodes = {1: [50, 30], 2: [100, 155], 3: [200, 155],
             4:[305, 110], 5: [110, 280], 6: [340, 275],
             7:[90, 430], 8:[230, 380], 9:[335, 475]}

    (v, q) = bfs([0, 0], list(nodes.values()))
    return v, q


def readIMG():
    global callBackImg
    cv.samples.addSamplesDataSearchPath(
        "/graph-traversal/")
    orig = cv.imread(cv.samples.findFile("minefield.jpg"))
    # orig = cv.imread("/graph-traversal/minefield-colored.png.jpg")
    print(orig)
    callBackImg = orig
    cv.imshow("Display window", orig)
    while True:
        k = cv.waitKey(1)
        cv.setMouseCallback('Display window', printRGB)
        if k == ord('s'):
            cv.imwrite('testSave.png', callBackImg)
        elif k == ord('q'):
            break


def main():
    """
    Main driver
    :return: None
    """
    # scale = 10
    #
    (img, path) = path_minefield()
    #
    # (height, width, channels) = img.shape
    # resize = cv.resize(img, (width * scale, height * scale))
    # (height, width) = resize.shape
    # resize = resize.reshape(height, width, 1)
    # rPath = []
    #
    # for p in path:
    #     rPath.append([p[0] * scale, p[1] * scale])
    #
    # print("Path", rPath)
    #
    # drawPath(resize, rPath)
    # showImage([resize])
    # readIMG()
    # print(path_minefield())

if __name__ == '__main__':
    main()
