#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

import math


# CONSTANTS
ROBOT_DIAMETER = 46.49
WHEEL_CIRCUMFERENCE = 17.28


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.

# Create your objects here.
ev3 = EV3Brick()

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
gyro_sensor = GyroSensor(Port.S1)

d = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=114.0) #might need to change last 2 params
d.settings(700, 100, 100, 100)

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
            path = "{}-{}".format(ids[len(ids) - 1], ids[0])
        else:
            angle = calculate_theta(positions[i + 1][0] - positions[i][0], positions[i + 1][1] - positions[i][1])
            path = "{}-{}".format(ids[i], ids[i+1])

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
            path = "{}-{}".format(ids[len(ids) - 1], ids[0])
        else:
            dist = calculate_dist(positions[i + 1], positions[i])
            path = "{}-{}".format(ids[i], ids[i+1])
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

def assign_mines(raw_pos):
    """
    Takes a list of raw positions of mines and converts it to a dictionary
    :param paths: The vertex paths in the form of "Vertex1-Vertex2"
    :param results: The calculations from the respective find_all functions
    :return: A dictionary where the key is the vertex path and the value is the respective result
    """
    # [[0, 10], [15, 20], [30, 10]]
    complete = {"S": [0, 0]}
    mine_pos = dict()
    for i, pos in enumerate(raw_pos):
        letter = chr(i + 65)
        print(letter)
        if letter == "S":
            letter = chr(i + 65 + 1)
        mine_pos[letter] = pos
    complete.update(mine_pos)
    return complete

def path_mines():
    mine_pos = {"S": [0, 0], "A": [13, 18], "B": [19, 14], "C": [40, 36]}
    angle1 = calculate_theta(mine_pos["A"][0], mine_pos["A"][1])
    dist1 = calculate_c(mine_pos["A"][0] * 10, mine_pos["A"][1] * 10)
    angle2 = calculate_theta(mine_pos["B"][0] - mine_pos["A"][0], mine_pos["B"][1] - mine_pos["A"][1])
    dist2 = calculate_c((mine_pos["B"][0] - mine_pos["A"][0]) * 10, (mine_pos["B"][1] - mine_pos["A"][1]) * 10)
    angle3 = calculate_theta(mine_pos["C"][0] - mine_pos["B"][0], mine_pos["C"][1] - mine_pos["B"][1])
    dist3 = calculate_c((mine_pos["C"][0] - mine_pos["B"][0]) * 10, (mine_pos["C"][1] - mine_pos["B"][1]) * 10)
    d.turn(angle1)
    d.straight(dist1)
    d.turn(angle2)
    d.straight(dist2)
    d.turn(angle3)
    d.straight(dist3)

def main():
    path_mines()

path_mines()

