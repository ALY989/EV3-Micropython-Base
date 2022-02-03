#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

import challengeTemplate

# Use the following links to access the documentation
# How to control the EV3: https://docs.pybricks.com/en/v2.0/hubs.html#pybricks.hubs.EV3Brick
# How to control the robot: https://docs.pybricks.com/en/v2.0/ev3devices.html
# How to implement timing and logging in your program: https://pybricks.com/ev3-micropython/tools.html
# Rule book: https://firstinspiresst01.blob.core.windows.net/first-forward/fll-challenge/fll-challenge-cargo-connect-robot-game-rulebook.pdf

# --- Begin Program ---
def start(ev3, robot,ultrasonicSensor):
    robot.straight(1000)
    while ultrasonicSensor.distance > 20:
        robot.drive(100,0)
    robot.straight(360)
    robot.turn(-90)