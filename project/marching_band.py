from utils import sound
from utils.brick import TouchSensor, wait_ready_sensors, EV3UltrasonicSensor, reset_brick, Motor, BP
from time import sleep

US_SENSOR = EV3UltrasonicSensor(1)

KILL_SWITCH = TouchSensor(3)
PLAY_NOTE_BUTTON = TouchSensor(2) 
ENABLE_DRUM_BUTTON = TouchSensor(4)

NXT_MOTOR_1 = Motor("C")
NXT_MOTOR_2 = Motor("B")

NXT_MOTOR_1.reset_position()
NXT_MOTOR_2.reset_position()

DELAY = 0.1

A5 = sound.Sound(duration=0.3, pitch="A5", volume=100)
A6 = sound.Sound(duration=0.3, pitch="A6", volume=100)
A7 = sound.Sound(duration=0.3, pitch="A7", volume=100)
A8 = sound.Sound(duration=0.3, pitch="A8", volume=100)

wait_ready_sensors(True) 

def do_drumming():
    do_drumming.count += 1

    if do_drumming.count % 3 == 0:
        NXT_MOTOR_1.set_position_relative(do_drumming.motor1_dir * 45)
        do_drumming.motor1_dir *= -1

    if do_drumming.count % 2 == 0:
        NXT_MOTOR_2.set_position_relative(do_drumming.motor2_dir * 45)
        do_drumming.motor2_dir *= -1

# "static" variables for function do_drumming
do_drumming.count = 0
do_drumming.motor1_dir = 1  # negative is toward ground
do_drumming.motor2_dir = 1  # positive is toward robot

def play_note(dist):
    if (dist == None):
        return 
    elif dist == 10:
        A7.play()
    elif dist == 20:
        A8.play()
    elif dist == 30:
        A6.play()
    elif dist == 40:
        A5.play()
    

def main():
    is_drumming = False
    current_distance = 10

    try:
        input("Press enter to begin")

        while True:
            sleep(DELAY)

            # buttons
            if ENABLE_DRUM_BUTTON.is_pressed():
                print("Drumming button pressed")
                is_drumming = not is_drumming
                sleep(0.2) # to avoid double presses
            if PLAY_NOTE_BUTTON.is_pressed():
                print(f"Play note button pressed: {current_distance} cm")
                play_note(current_distance)
            if KILL_SWITCH.is_pressed():
                print("Kill switch pressed")
                break

            # actions
            if is_drumming:
                do_drumming()

            # distance
            current_distance = US_SENSOR.get_cm()
            if (current_distance < 8):
                current_distance = None
                print("Wrong note")
            elif (current_distance < 15):
                current_distance = 10
            elif current_distance < 25:
                current_distance = 20
            elif current_distance < 33:
                current_distance = 30
            elif (current_distance < 50):
                current_distance = 40
            else:
                current_distance = None
                print("Wrong note")


    except KeyboardInterrupt:
        print("Closing program now")

    except BaseException as e:
        print(e)

    finally:
        NXT_MOTOR_1.set_position(0)
        NXT_MOTOR_2.set_position(0)
        sleep(0.5)
        reset_brick()
        exit(0)


if __name__ == '__main__':
    main()
