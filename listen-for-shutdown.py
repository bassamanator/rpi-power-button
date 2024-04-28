import wiringpi as wp
from wiringpi import GPIO
import time
import subprocess


def shutdown():
    print("Shutting down")
    subprocess.call(["shutdown", "-h", "now"], shell=False)


def main():
    LED = 3
    BUTTON = 2
    BUTTON_PRESS_DELAY = 5

    try:
        wp.wiringPiSetup()
        wp.pinMode(LED, GPIO.OUTPUT)
        wp.pinMode(BUTTON, GPIO.INPUT)
        wp.pullUpDnControl(BUTTON, GPIO.PUD_UP)

        wp.digitalWrite(LED, GPIO.HIGH)  # initial state

        while True:
            wp.delay(100)
            BUTTON_STATE = wp.digitalRead(BUTTON)
            print("checkless button states is: " + str(BUTTON_STATE))

            time_start = time.time()
            time_button = 0
            led_state = GPIO.LOW

            while (
                wp.digitalRead(BUTTON) == GPIO.LOW and time_button <= BUTTON_PRESS_DELAY
            ):
                print("starting count")
                print("Button:", time_button, led_state)

                wp.digitalWrite(LED, led_state)
                led_state = not led_state
                time.sleep(0.1)

                time_button = time.time() - time_start

            wp.digitalWrite(LED, GPIO.HIGH)  # just in case it was low

            if time_button >= BUTTON_PRESS_DELAY:
                break

        shutdown()

    except Exception as e:
        print(e)
    except KeyboardInterrupt:
        print("Goodbye")


if __name__ == "__main__":
    main()
