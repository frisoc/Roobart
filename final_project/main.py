#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# CONSTANTS
ROBOT_DIAMETER = 46.49
WHEEL_CIRCUMFERENCE = 17.28

ev3 = EV3Brick()

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
color_sensor = ColorSensor(Port.S3)

d = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=110)  # might need to change last 2 params
d.settings(700, 100, 100, 100)


def detect_bombs(straight_dist, turn_dist, x_dist, y_dist, bomb_color):
    """
    Maps a field of mines in a defined area
    :param straight_dist: The distance to travel when moving straight
    :param turn_dist: The distance to move forward when at a turn
    :param x_dist: The total distance to travel in the x-direction
    :param y_dist: The total distance to travel in the y-direction
    :param bomb_color: The color of the bombs
    :return: The list of the bomb positions as a list of lists
    """
    positions = [0, 0]  # (x, y)
    points = []
    direction = 1
    while 0 <= positions[0] <= x_dist:
        while 0 <= positions[1] <= y_dist:
            d.straight(straight_dist)

            if color_sensor.color() == bomb_color:
                points.append([positions[0], positions[1]])
                ev3.speaker.say("Bomb Detected")
                print(positions[0], positions[1])
                print(points)

            if direction == 1:
                positions = (positions[0], positions[1] + straight_dist)
            else:
                positions = (positions[0], positions[1] - straight_dist)

        if positions[1] + straight_dist > y_dist:
            positions = (positions[0], y_dist)
        elif positions[1] - straight_dist < 0:
            positions = (positions[0], 0)

        d.turn(90 * direction)
        d.straight(turn_dist)
        d.turn(90 * direction)
        positions = (positions[0] + turn_dist, positions[1])
        direction = direction * -1

    ev3.speaker.say("Scan complete")
    return points


# straight_dist = 10
# turn_dist = 15
# x_dist = 100
# y_dist = 100
# bomb = Color.WHITE
# field = Color.BLUE

straight = 10
turn = 15
x_length = 3 * 10  # Dist in in mm
y_length = 3 * 10  # Dist in in mm
bomb = Color.WHITE

positions = detect_bombs(straight, turn, x_length, y_length, bomb)

print("List of bomb positions:", positions)

# Testing for color detection
# print("color 1: ", color_sensor.color())
# ev3.speaker.say("Detecting Color")
# d.straight(150)
# print('color 2: ', color_sensor.color())
# ev3.speaker.say("Detecting Color")
