from utils import sound
from utils.brick import TouchSensor, wait_ready_sensors, EV3UltrasonicSensor, reset_brick, Motor, BP
from time import sleep

WHEEL_MOTOR = Motor("B")

WHEEL_MOTOR.reset_position()


wait_ready_sensors(True) 


def main():
    try:
        input("enter something to start")

        while (True):
            input("press to move a bit")
            WHEEL_MOTOR.set_position_relative(100)
    except KeyboardInterrupt:
        print("Ending program")
    except Exception as e:  # capture all exceptions including KeyboardInterrupt (Ctrl-C)
        print("Exception: ", e)

if __name__ == '__main__':
    main()


