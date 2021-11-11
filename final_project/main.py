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

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.

# Create your objects here.
ev3 = EV3Brick()

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
color_sensor = ColorSensor(Port.S3)

d = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=110)  # might need to change last 2 params
d.settings(700, 100, 100, 100)


# # functions

# def detect_bombs(granularity, turn_distance, edge_distance, bomb_color, field_color):
#     """
#     granularity: How far the robot will step forward when traveling along y in mm
#     turn_distance: How far the robot will step after turning 90 degrees in mm
#     edge_distance: distance of each edge of area in mm
#     bomb_color: color of the bombs
#     field_color: color of the field
#     return: list of points
#     """
#     total_y = 0
#     total_x = 0
#     # bomb_color = Color.BLUE
#     # field_color = Color.BLACK
#     points = []
#     direction = 1
#     while total_x <= edge_distance:
#         while total_y <= edge_distance:
#             d.straight(granularity)
#             if color_sensor.color() == bomb_color:
#                 points.append([total_x, total_y])
#                 ev3.speaker.say("Bomb Detected")
#                 print(total_x, total_y)
#                 print(points)
#             total_y += granularity
#         total_y = 0
#         d.turn(90 * direction)
#         d.straight(turn_distance)
#         d.turn(90 * direction)
#         total_x += turn_distance
#         direction = direction * -1
#     ev3.speaker.say("Scan complete")
#     return points

# # write your program here
# granularity = 150
# turn_distance = 200
# edge_distance = 400

# # points = detect_bombs(granularity, turn_distance, edge_distance, Color.BLACK, Color.BROWN)
# points = detect_bombs(granularity, turn_distance, edge_distance, Color.WHITE, Color.BLUE)
# print(points)
# # print("color 1: ", color_sensor.color())
# # ev3.speaker.say("Detecting Color")
# # d.straight(150)
# # print('color 2: ', color_sensor.color())
# # ev3.speaker.say("Detecting Color")

def detect_bombs(straight_dist, turn_dist, x_dist, y_dist, bomb_color, field_color):
    """
    granularity: How far the robot will step forward when traveling along y in mm
    turn_distance: How far the robot will step after turning 90 degrees in mm
    edge_distance: distance of each edge of area in mm
    bomb_color: color of the bombs
    field_color: color of the field
    return: list of points
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

    print(positions)
    ev3.speaker.say("Scan complete")
    return points


# straight_dist = 10
# turn_dist = 15
# x_dist = 100
# y_dist = 100
# bomb = Color.WHITE
# field = Color.BLUE

straight_dist = 10
turn_dist = 15
x_dist = 3 * 10  # Dist in in mm
y_dist = 3 * 10  # Dist in in mm
bomb = Color.WHITE
field = Color.BLUE

detect_bombs(straight_dist, turn_dist, x_dist, y_dist, bomb, field)