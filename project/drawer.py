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

POWER_LIMIT = 80
SPEED_LIMIT = 240
HORIZONTAL_DISTANCE = 112
SLEEP_INPUT = 0.1
SLEEP_TIME_SMALL = 0.5

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
            if not randomize:
                one_pressed = False
                zero_pressed = False
                while True:
                    sleep_with_killswitch(SLEEP_INPUT)
                    if ONE_BUTTON.is_pressed() or ZERO_BUTTON.is_pressed():
                        one_pressed = ONE_BUTTON.is_pressed()
                        zero_pressed = ZERO_BUTTON.is_pressed()
                        while ONE_BUTTON.is_pressed() or ZERO_BUTTON.is_pressed():
                            pass
                        break
                
                if one_pressed and zero_pressed:
                    randomize = True
                elif one_pressed:
                    out[row].append(1)
                elif zero_pressed:
                    out[row].append(0)

                print(out)

            if randomize:
                randomBit = random.randint(0, 1)
                if (randomBit == 1):
                    oneCount += 1
                if (oneCount < 15):
                    out[row].append(randomBit)
                else:
                    out[row].append(0)
                continue

    if (oneCount > 15):
        print("Too many 1s entered")
        exit(1)
    return out


def sleep_with_killswitch(t):
    first = time()
    while (True):
        if (KILL_SWITCH.is_pressed()):
            raise Exception("Kill switch has been pressed")
        end = time()
        if (end - first >= t):
            return

def loadCube():
    """function to load cube, retract slightly to load"""
    set_pos_and_wait(PISTON_MOTOR, -160)
    set_pos_and_wait(PISTON_MOTOR, 0)

def set_pos_and_wait(motor, pos):
    motor.set_position(pos)
    while abs(motor.get_position() - pos) > 2:
        if (KILL_SWITCH.is_pressed()):
            raise Exception("Kill switch has been pressed")

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
    set_pos_and_wait(PISTON_MOTOR, rotDist)
    set_pos_and_wait(PISTON_MOTOR, 0)

def moveRobot():
    WHEEL_MOTOR.set_position_relative(HORIZONTAL_DISTANCE)
    return


def main():
    matrix = getInputMatrix()

    print("To be printed:")
    for row in matrix:
        print(row)
    
    sleep_with_killswitch(2)

    try:
        for row in range(len(matrix)):
            for cube in range(len(matrix[0]) - 1, -1, -1):
                # cube = number of representing distant (0..4)
                if (matrix[row][cube] == 1):
                    sleep_with_killswitch(SLEEP_TIME_SMALL)
                    loadCube()
                    sleep_with_killswitch(SLEEP_TIME_SMALL)
                    pushCube(cube)    
            moveRobot()
            sleep_with_killswitch(SLEEP_TIME_SMALL)

    except KeyboardInterrupt as e:
        print(e)
        exit(1)
    except Exception as e:
        print(e)
        exit(1)
    finally:
        set_pos_and_wait(PISTON_MOTOR, 0)
        set_pos_and_wait(WHEEL_MOTOR, 0)
        reset_brick()


if __name__ == "__main__":
    main()

