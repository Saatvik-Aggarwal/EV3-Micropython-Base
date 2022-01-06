#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

def doChallenge(robot):
    # travel in a square
    robot.straight(500)
    robot.turn(90)
    robot.straight(500)
    robot.turn(90)
    robot.straight(500)
    robot.turn(90)
    robot.straight(500)


