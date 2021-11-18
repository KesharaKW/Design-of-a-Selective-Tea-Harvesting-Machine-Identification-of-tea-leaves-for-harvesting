from picamera import PiCamera
from time import sleep
import cv2

camera = PiCamera()
camera.rotation = 180

camera.start_preview()
sleep(5)
camera.stop_preview()