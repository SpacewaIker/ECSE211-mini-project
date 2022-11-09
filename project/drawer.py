from utils import sound
from utils.brick import TouchSensor, wait_ready_sensors, EV3UltrasonicSensor, reset_brick, Motor, BP
from time import sleep
import random

WHEEL_MOTOR = Motor("B")
PISTON_MOTOR = Motor("C")
ZERO_BUTTON = TouchSensor(3)
ONE_BUTTON = TouchSensor(2) 

WHEEL_MOTOR.reset_position()
PISTON_MOTOR.reset_position()

POWER_LIMIT = 70
SPEED_LIMIT = 70
HORIZONTAL_DISTANCE = 112
SLEEP_TIME = 0.1


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
                if (not randomize):
                    inp = input("enter 1 or 0: ")
                else:
                    randomBit = random.randint(0, 1)
                    if (randomBit == 1):
                        oneCount += 1
                    if (oneCount < 15):
                        out[row].append(randomBit)
                    else:
                        out[row].append(0)
                    break
                # if (ZERO_BUTTON.is_pressed()):
                #     out[row][bit] = 0
                #     break
                # if (ONE_BUTTON.is_pressed()):
                #     out[row][bit] = 1
                #     break
                if (inp == "01"):
                    randomize = True
                if (inp == "0"):
                    out[row].append(0)
                    break
                if (inp == "1"):
                    oneCount += 1
                    out[row].append(1)
                    break
    if (oneCount > 15):
        print("Too many 1s entered")
        exit(1)
    return out


def loadCube():
    """function to load cube, retract slightly to load"""
    pass

def pushCube(distance):
    """function to move piston to distance and retract"""
    pass

def moveRobot():
    WHEEL_MOTOR.set_position_relative(HORIZONTAL_DISTANCE)
    return


def main():
    matrix = getInputMatrix()
    try:
        WHEEL_MOTOR.set_limits(power = POWER_LIMIT, dps = SPEED_LIMIT)
        PISTON_MOTOR.set_limits(power = POWER_LIMIT, dps = SPEED_LIMIT)
        # PISTON_MOTOR.set_limits(power = POWER_LIMIT, dps = SPEED_LIMIT)
        for row in range(len(matrix)):
            for cube in range(len(matrix[0]), 0, -1):
                # cube = number of representing distant (0..4)
                if (matrix[row][cube] == 1):
                    loadCube()
                    pushCube(cube)    
                sleep(SLEEP_TIME)
            moveRobot()
            sleep(SLEEP_TIME)

                



    except KeyboardInterrupt as e:
        print(e)
        exit(1)
    except Exception as e:
        print(e)
        exit(1)
    finally:
        WHEEL_MOTOR.set_position(0)
        PISTON_MOTOR.set_position(0)


if __name__ == "__main__":
    main()

