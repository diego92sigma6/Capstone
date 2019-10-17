import RPi.GPIO as GPIO
from ReadingsHUB import *

def main():
    print("starting system")

    #setup GPIOs
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)

    readingsHUB = ReadingsHUB()
    while True:
        pass

if __name__ == "__main__":
    main()
