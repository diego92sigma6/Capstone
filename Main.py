'''
Author Diego Marquez

File that orchestrates all the processes running on the system
Subprocesses stdout is handled by adding a tag to indicate where 
the log comes from

The webapp subprocess is commented out because the demonstration
had the webapp running on a different computer, although it 
made API calls to the raspberry
'''


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
    t = threading.Thread(target=output_reader, args=(proc, '[REST]'))
    t.start()
    #print("starting Webapp")
    #proc2 = subprocess.Popen(['npm', 'start',  '--prefix' , '/home/pi/Capstone/webapp'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    #t2 = threading.Thread(target=output_reader, args=(proc2, '[WEB]'))
    #t2.start()

def main():

    print("starting system")
    startServers()

    #setup GPIOs
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)

    readingsHUB = ReadingsHUB()

    while True:
        pass

if __name__ == "__main__":
    main()
