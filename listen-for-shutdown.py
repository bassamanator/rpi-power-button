#!/usr/bin/env python

# https://github.com/WiringPi/WiringPi-Python/
import wiringpi as wp
from wiringpi import GPIO
import time
import subprocess


def shutdown():
    print("Shutting down")
    subprocess.call(["shutdown", "-h", "now"], shell=False)


def main():
    LED = 3  # NOTE wPI: 3; Physical: 8
    BUTTON = 2  # NOTE wPI: 2; Physical: 7
    BUTTON_PRESS_DELAY = 3  # NOTE seconds

    try:
        wp.wiringPiSetup()
        wp.pinMode(LED, GPIO.OUTPUT)
        wp.pinMode(BUTTON, GPIO.INPUT)
        wp.pullUpDnControl(BUTTON, GPIO.PUD_UP)

        wp.digitalWrite(LED, GPIO.HIGH)  # initial state

        while True:
            wp.delay(100)

            time_start = time.time()
            button_press_timer = 0
            led_state = GPIO.LOW

            while (
                wp.digitalRead(BUTTON) == GPIO.LOW
                and button_press_timer <= BUTTON_PRESS_DELAY
            ):
                # print("Button:", button_press_timer, led_state)  # NOTE for debugging

                wp.digitalWrite(LED, led_state)
                led_state = not led_state
                time.sleep(0.1)

                button_press_timer = time.time() - time_start

            wp.digitalWrite(LED, GPIO.HIGH)  # NOTE just in case it was low

            if button_press_timer >= BUTTON_PRESS_DELAY:
                break

        shutdown()

    except Exception as e:
        print(e)
    except KeyboardInterrupt:
        print("CTRL+C")
    finally:
        print("End program")


if __name__ == "__main__":
    main()
