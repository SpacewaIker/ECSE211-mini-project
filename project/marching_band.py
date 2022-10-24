from utils import sound
from utils.brick import TouchSensor, wait_ready_sensors, EV3UltrasonicSensor, reset_brick, Motor, BP
from time import sleep

US_SENSOR = EV3UltrasonicSensor(1)

KILL_SWITCH = TouchSensor(3)
PLAY_NOTE_BUTTON = TouchSensor(2) 
ENABLE_DRUM_BUTTON = TouchSensor(4)

NXT_MOTOR_1 = Motor("C")
NXT_MOTOR_2 = Motor("B")

DELAY = 0.1

wait_ready_sensors(True) 

is_drumming = False

def do_drumming():
    do_drumming.count += 1

    if do_drumming.count % 4 == 0:
        if do_drumming.motor1_is_up:
            NXT_MOTOR_1.set_position_relative(-50)
        else:
            NXT_MOTOR_1.set_position_relative(50)

    if do_drumming.count % 2 == 0:
        if do_drumming.motor2_is_up:
            NXT_MOTOR_2.set_position_relative(-50)
        else:
            NXT_MOTOR_2.set_position_relative(50)

# "static" variables for function do_drumming
do_drumming.count = 0
do_drumming.motor1_is_up = False
do_drumming.motor2_is_up = False


def main():
    try:
        input("Press any key to begin")

        while True:
            sleep(DELAY)

            # buttons
            if ENABLE_DRUM_BUTTON.is_pressed():
                is_drumming = not is_drumming
            if PLAY_NOTE_BUTTON.is_pressed():
                pass
            if KILL_SWITCH.is_pressed():
                print("Kill switch pressed")
                break

            # actions
            if is_drumming:
                do_drumming()


    except KeyboardInterrupt:
        print("Closing program now")

    finally:
        reset_brick()
        exit(0)


if __name__ == '__main__':
    main()
