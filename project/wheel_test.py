# from utils import sound
# from utils.brick import TouchSensor, wait_ready_sensors, EV3UltrasonicSensor, reset_brick, Motor, BP
# from time import sleep
import random

# WHEEL_MOTOR = Motor("B")
# ZERO_BUTTON = TouchSensor(3)
# ONE_BUTTON = TouchSensor(2) 

# WHEEL_MOTOR.reset_position()

# wait_ready_sensors(True) 

def getInputMatrix(): # returns 5x5 matrix
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

    return out



# def main():
#     try:
#         input("enter something to start")
#         WHEEL_MOTOR.set_limits(power = 70, dps = 70)
#         while (True):
#             inp = input("press to move a bit")
#             if (inp == "x"):
#                 break
#             WHEEL_MOTOR.set_position_relative(112)
#     except KeyboardInterrupt:
#         print("Ending program")
#     except Exception as e:  # capture all exceptions including KeyboardInterrupt (Ctrl-C)
#         print("Exception: ", e)

#     finally:
#         WHEEL_MOTOR.set_position(0)

if __name__ == '__main__':
    # main()
    matrix = getInputMatrix()
    print(matrix)


