import RPi.GPIO as GPIO
import subprocess
import threading
from ReadingsHUB import ReadingsHUB


def output_reader(proc, tag):
    for line in iter(proc.stdout.readline, b''):
        #print('got line: {0}'.format(line.decode('utf-8')), end='')
        line = line.replace('\n','')
        print('{1} {0}'.format(line.decode('utf-8'), tag))

def startServers():

    #REST API
    print("starting REST API")
    proc = subprocess.Popen(['python', '-u', './RestAPI.py'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    print("starting Webapp")
    proc2 = subprocess.Popen(['npm', 'start',  '--prefix' , '/home/pi/Capstone/webapp'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    t2 = threading.Thread(target=output_reader, args=(proc2, '[WEB]'))
    t2.start()
    t = threading.Thread(target=output_reader, args=(proc, '[REST]'))
    t.start()

def main():


    print("starting system")
    #startServers()

    #setup GPIOs
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)

    readingsHUB = ReadingsHUB()

    while True:
        pass

if __name__ == "__main__":
    main()
