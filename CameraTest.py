from picamera import PiCamera
from time import sleep
import numpy as np

camera = PiCamera()
camera.resolution = (320,240)
camera.framerate = 24
camera.start_preview(alpha=200)
sleep(50)
#camera.stop_preview()
#picBuffer = np.empty((240, 320, 3), dtype=np.uint8)
#camera.capture(picBuffer, 'rgb')
#print(picBuffer)
