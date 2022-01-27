#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

import challengeTemplate

import andy
import ALY989
# Use the following links to access the documentation
# How to control the EV3: https://docs.pybricks.com/en/v2.0/hubs.html#pybricks.hubs.EV3Brick
# How to control the robot: https://docs.pybricks.com/en/v2.0/ev3devices.html
# How to implement timing and logging in your program: https://pybricks.com/ev3-micropython/tools.html
# Rule book: https://firstinspiresst01.blob.core.windows.net/first-forward/fll-challenge/fll-challenge-cargo-connect-robot-game-rulebook.pdf

# --- Begin Example Program ---

# Initialize the EV3 Brick.
ev3 = EV3Brick()

# Initialize the motors. Initialize motors using the ports
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
#sensors are initialized by doing S and then the number
UltrasonicSensor = UltrasonicSensor(S1)

# Initialize the drive base. 
# MIGHT WANT TO CHECK TO MAKE SURE THIS IS RIGHT
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

#Start of the program. Press left button if the robot is on the left side. Press the right button if the robot is on the right side.
ALY989.start()
# --- End Example Program ---