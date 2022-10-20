from utils import sound
from utils.brick import TouchSensor, wait_ready_sensors, EV3UltrasonicSensor, reset_brick, Motor, BP
from time import sleep

US_SENSOR = EV3UltrasonicSensor(1)

KILL_SWITCH = TouchSensor(3)
PLAY_NOTE_BUTTON = TouchSensor(2) 
ENABLE_DRUM_BUTTON = TouchSensor(4)

NXT_MOTOR_1 = Motor("C")
NXT_MOTOR_2 = Motor("B")

wait_ready_sensors(True) 

is_drumming = False

def toggle_drumming():    
    if (is_drumming):
        NXT_MOTOR_2.set_power(20)
        while True:
            pass
    else:
    
        pass


    is_drumming = not is_drumming




def main():
    pass


if __name__ == '__main__':
    main()

