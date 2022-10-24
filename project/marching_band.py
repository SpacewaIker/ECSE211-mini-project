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

A4 = sound.Sound(duration=0.3, pitch="A4", volume=85)
C4 = sound.Sound(duration=0.3, pitch="C4", volume=85)
E4 = sound.Sound(duration=0.3, pitch="E4", volume=85)
A5 = sound.Sound(duration=0.3, pitch="A5", volume=85)

wait_ready_sensors(True) 

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

def play_note(dist):
    if dist == 10:
        A4.play()
        A4.wait_done()
    elif dist == 20:
        C4.play()
        C4.wait_done()
    elif dist == 30:
        E4.play()
        E4.wait_done()
    elif dist == 40:
        A5.play()
        A5.wait_done()
    

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
            if PLAY_NOTE_BUTTON.is_pressed():
                print("Play note button pressed")
                play_note(current_distance)
            if KILL_SWITCH.is_pressed():
                print("Kill switch pressed")
                break

            # actions
            if is_drumming:
                do_drumming()

            # distance
            current_distance = US_SENSOR.get_distance()
            if current_distance < 15:
                current_distance = 10
            elif current_distance < 25:
                current_distance = 20
            elif current_distance < 35:
                current_distance = 30
            else:
                current_distance = 40


    except KeyboardInterrupt:
        print("Closing program now")

    except BaseException as e:
        print(e)

    finally:
        reset_brick()
        exit(0)


if __name__ == '__main__':
    main()
