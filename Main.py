import RPi.GPIO as GPIO
import subprocess
import threading
from ReadingsHUB import *


def output_reader(proc):
    for line in iter(proc.stdout.readline, b''):
        #print('got line: {0}'.format(line.decode('utf-8')), end='')
        line = line.replace('\n','')
        print('[REST] {0}'.format(line.decode('utf-8')))

def main():

    print("starting REST API")
    #REST API
    proc = subprocess.Popen(['python', '-u', './RestAPI.py'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    t = threading.Thread(target=output_reader, args=(proc,))
    t.start()

    print("starting system")

    #setup GPIOs
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)

    readingsHUB = ReadingsHUB()

    while True:
        pass

if __name__ == "__main__":
    main()
