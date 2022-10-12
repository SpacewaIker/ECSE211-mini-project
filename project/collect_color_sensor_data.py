#!/usr/bin/env python3

"""
This test is used to collect data from the color sensor.
It must be run on the robot.
"""

# Add your imports here, if any
from utils.brick import EV3ColorSensor, wait_ready_sensors, TouchSensor, reset_brick
from time import sleep

COLOR_SENSOR_DATA_FILE = "../data_analysis/group1/red_color.csv"
DELAY_SEC = 0.15  # button sampling rate
# complete this based on your hardware setup
COLOR_SENSOR = EV3ColorSensor(1)
TOUCH_SENSOR = TouchSensor(2)

wait_ready_sensors(True) # Input True to see what the robot is trying to initialize! False to be silent.


def collect_color_sensor_data():
    """Collect color sensor data."""
    try:
        output_file = open(COLOR_SENSOR_DATA_FILE, "w")
        while not TOUCH_SENSOR.is_pressed():
            pass  # do nothing while waiting for first button press
        print("Touch sensor pressed")
        sleep(1)
        print("Starting to collect color samples")
        count = 0
        while True:
            sleep(DELAY_SEC)
            if TOUCH_SENSOR.is_pressed():
                while not TOUCH_SENSOR.is_released():
                    pass
                count += 1
                col_data = COLOR_SENSOR.get_value()  # Float value in centimeters 0, capped to 255 cm
                if col_data is not None:  # If None is given, then data collection failed that time
                    r,g,b,a = col_data
                    print((r, g, b))
                    print(count)
                    output_file.write(f"{r, g, b}\n")
            
    except BaseException:  # capture all exceptions including KeyboardInterrupt (Ctrl-C)
        pass
    finally:
        print("Done collecting color samples")
        output_file.close()
        reset_brick()  # Turn off everything on the brick's hardware, and reset it
        exit()


if __name__ == "__main__":
    collect_color_sensor_data()
