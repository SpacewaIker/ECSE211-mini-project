from utils import sound
from utils.brick import TouchSensor, wait_ready_sensors, EV3UltrasonicSensor, reset_brick, Motor, BP
from time import sleep
from time import time
import random

WHEEL_MOTOR = Motor("B")
PISTON_MOTOR = Motor("C")
ONE_BUTTON = TouchSensor(3) 
ZERO_BUTTON = TouchSensor(2)
KILL_SWITCH = TouchSensor(4)

WHEEL_MOTOR.reset_position()
PISTON_MOTOR.reset_position()

POWER_LIMIT = 70
SPEED_LIMIT = 90
HORIZONTAL_DISTANCE = 112
SLEEP_TIME_SMALL = 1
SLEEP_TIME_BIG = 2
SLEEP_TIME_BIGGER = 4

WHEEL_MOTOR.set_limits(power = POWER_LIMIT, dps = SPEED_LIMIT)
PISTON_MOTOR.set_limits(power = POWER_LIMIT, dps = SPEED_LIMIT)

wait_ready_sensors(True) 

def getInputMatrix():
    """Returns 5x5 matrix"""
    out = []
    randomize = False
    oneCount = 0
    for row in range(5):
        out.append([])
        for _ in range(5):
            while (True):
                sleep(SLEEP_TIME_BIG)
                if (not randomize):
                    print("Press a button")
                    while (not ONE_BUTTON.is_pressed() and not ZERO_BUTTON.is_pressed()):
                        pass
                    if (ZERO_BUTTON.is_pressed() and ONE_BUTTON.is_pressed()):
                        while (ZERO_BUTTON.is_pressed() and ONE_BUTTON.is_pressed()):
                            pass
                        print("You have randomized the selection")
                        randomize = True

                    if (ZERO_BUTTON.is_pressed()):
                        while ZERO_BUTTON.is_pressed():
                            pass
                        out[row].append(0)
                        print("You have pressed 0")
                        break

                    if (ONE_BUTTON.is_pressed()):
                        while ONE_BUTTON.is_pressed():
                            pass
                        print("You have pressed 1")
                        out[row].append(1)
                        break

                else:
                    randomBit = random.randint(0, 1)
                    if (randomBit == 1):
                        oneCount += 1
                    if (oneCount < 15):
                        out[row].append(randomBit)
                    else:
                        out[row].append(0)
                    break

    if (oneCount > 15):
        print("Too many 1s entered")
        exit(1)
    return out


def ourSleep(t):
    first = time()
    while (True):
        if (KILL_SWITCH.is_pressed()):
            raise Exception("Kill switch has been pressed")
        end = time()
        if (end - first >= t):
            return

def loadCube():
    """function to load cube, retract slightly to load"""
    PISTON_MOTOR.set_position(-210)
    ourSleep(SLEEP_TIME_BIG)
    PISTON_MOTOR.set_position(0)
    ourSleep(SLEEP_TIME_BIG)
    pass

def pushCube(distance):
    """function to move piston to distance and retract"""
    rotDist = 0
    if (distance == 0):
        rotDist = 142
    elif (distance == 1):
        rotDist = 254
    elif (distance == 2):
        rotDist = 366
    elif (distance == 3):
        rotDist = 478
    elif (distance == 4):
        rotDist = 590
    PISTON_MOTOR.set_position(rotDist)
    while (PISTON_MOTOR.get_position() < rotDist - 1):
        pass

    PISTON_MOTOR.set_position(0)
    while PISTON_MOTOR.get_position() > 1:
        pass

def moveRobot():
    WHEEL_MOTOR.set_position_relative(HORIZONTAL_DISTANCE)
    return


def main():
    # matrix = getInputMatrix()
    matrix = [
        [0,0,0,0,0],
        [1,1,1,1,1],
        [0,1,0,1,0],
        [0,1,0,1,0],
        [0,0,1,0,1],
    ]
    print(matrix)
    input("press enter to start")
    try:
        # PISTON_MOTOR.set_limits(power = POWER_LIMIT, dps = SPEED_LIMIT)
        for row in range(len(matrix)):
            for cube in range(len(matrix[0]) - 1, -1, -1):
                if (KILL_SWITCH.is_pressed()):
                    raise Exception("Kill switch has been pressed")
                # cube = number of representing distant (0..4)
                if (matrix[row][cube] == 1):
                    ourSleep(SLEEP_TIME_BIG)
                    loadCube()
                    ourSleep(SLEEP_TIME_BIG)
                    print(cube)
                    pushCube(cube)    
                ourSleep(SLEEP_TIME_BIG)
            moveRobot()
            ourSleep(SLEEP_TIME_SMALL)

                



    except KeyboardInterrupt as e:
        print(e)
        exit(1)
    except Exception as e:
        print(e)
        exit(1)
    finally:
        WHEEL_MOTOR.set_position(0)
        PISTON_MOTOR.set_position(0)
        reset_brick()
        exit(1)


if __name__ == "__main__":
    main()

