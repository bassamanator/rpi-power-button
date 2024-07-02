#!/usr/bin/env python
# import RPi.GPIO as GPIO
import subprocess
import time
from gpiozero import Button, LED

# from gpiozero import LED


print("Raspberry PI GPIO Button & LED Shutdown Script")

# Pin Definitions
PIN_LED = 4  # GPIO4 / Pin #7
PIN_BUTTON = 3  # GPIO3 / Pin #5
TIME_PRESSED_MAX = 3  # seconds

LED_ = LED(PIN_LED)
POWER_BUTTON = Button(PIN_BUTTON, hold_time=TIME_PRESSED_MAX)

try:

    def button_pressed():
        print("button was pressed")
        # Blink LED
        while True:
            LED_.off()
            time.sleep(0.1)
            LED_.on()
            time.sleep(0.1)

    def button_released():
        print("button was released")
        LED_.on()

    def do_shutdown():
        print("Shutting down...")
        subprocess.call(["shutdown", "-h", "now"], shell=False)  # Power Off

    LED_.on()
    # GPIO.setup(PIN_LED, GPIO.OUT, initial=GPIO.HIGH)  # LED ON
    # GPIO.setup(PIN_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Button
    # POWER_BUTTON = Button(PIN_BUTTON, hold_time=TIME_PRESSED_MAX)

    # # Button Press Event
    # GPIO.add_event_detect(
    #     PIN_BUTTON, GPIO.FALLING, callback=button_interupt, bouncetime=100
    # )

    POWER_BUTTON.when_pressed = button_pressed
    POWER_BUTTON.when_released = button_released
    POWER_BUTTON.when_held = do_shutdown

    # Sleep Forever, to keep script alive, button_interupt handles everything.
    while True:
        time.sleep(86400)

except Exception as e:
    print(e)
except KeyboardInterrupt:
    print("CTRL+C")
finally:
    print("End program")
