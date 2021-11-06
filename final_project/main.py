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
color_sensor = ColorSensor(Port.S1)

d = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=114.0) #might need to change last 2 params
d.settings(700, 100, 100, 100)

# functions

def detect_bombs(granularity, turn_distance, edge_distance, bomb_color, field_color):
    """
    granularity: How far the robot will step forward when traveling along y in mm
    turn_distance: How far the robot will step after turning 90 degrees in mm
    edge_distance: distance of each edge of area in mm
    bomb_color: color of the bombs
    field_color: color of the field
    return: list of points
    """
    total_y = 0
    total_x = 0
    # bomb_color = Color.BLUE
    # field_color = Color.BLACK
    points = []
    direction = 1
    while total_x <= edge_distance:
        while total_y <= edge_distance:
            d.straight(granularity)
            if color_sensor.color() == bomb_color:
                points.append([total_x, total_y])
                ev3.speaker.say("Bomb Detected")
                print(total_x, total_y)
                print(points)
            total_y += granularity
        total_y = 0
        d.turn(90 * direction)
        d.straight(turn_distance)
        d.turn(90 * direction)
        total_x += turn_distance
        direction = direction * -1
    ev3.speaker.say("Scan complete")
    return points

# write your program here
granularity = 150
turn_distance = 150 
edge_distance = 300 

points = detect_bombs(granularity, turn_distance, edge_distance, Color.BLACK, Color.BROWN)
print(points)
# print("color 1: ", color_sensor.color())
# ev3.speaker.say("Detecting Color")
# d.straight(150)
# print('color 2: ', color_sensor.color())
# ev3.speaker.say("Detecting Color")
