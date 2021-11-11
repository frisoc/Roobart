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

# [[0, 10], [15, 20], [30, 10]]

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.

# Create your objects here.
ev3 = EV3Brick()

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
# gyro_sensor = GyroSensor(Port.S1)

d = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=114.0) #might need to change last 2 params
d.settings(700, 100, 100, 100)

def path_mines():
    angles = {'S-A': 90.0, 'A-B': 33.690067525979785, 'B-C': -33.690067525979785, 'C-S': 18.43494882292201}
    dists = {'S-A': 10.0, 'A-B': 18.027756377319946, 'B-C': 18.027756377319946, 'C-S': 31.622776601683793}

    angles_list = list(angles.values())
    dists_list = list(dists.values())

    print(dists_list)

    for i in range(len(angles_list)):
        d.turn(angles_list[i])
        d.straight(dists_list[i])

def main():
    path_mines()

main()

