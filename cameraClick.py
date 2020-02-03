from picamera import PiCamera
from time import sleep
import RPi.GPIO as gpio
import datetime

gpio.setmode(gpio.BCM)

#Buttons Connected 
gpio.setup(17, gpio.IN, pull_up_down=gpio.PUD_UP)
gpio.setup(18, gpio.IN, pull_up_down=gpio.PUD_UP)

# Initialize 
camera= PiCamera()
camera.exposure_mode = 'antishake'

	
while True:
	
	#button presses
	inputVideo = gpio.input(17)
	inputCamera = gpio.input(18)

	# Video Button is Pressed
	if inputVideo == False:
		print('Video Button Pressed')
		camera.start_recording('/home/pi/Documents/' +  datetime.datetime.now().strftime('%Y-%m-%d%H:%M:%S') + '.h264')
		sleep(10)
		camera.stop_recording()
		sleep(.2)
		print('Video Capture Done')

	#  Camera Button is Pressed 
	if inputCamera == False:
		print('Camera Button Pressed')
		camera.capture('/home/pi/Documents/' +  datetime.datetime.now().strftime('%Y-%m-%d%H:%M:%S') + '.png')
		sleep(.2)

