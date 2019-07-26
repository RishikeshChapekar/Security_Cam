import RPi.GPIO as GPIO
import os
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)         

 
while True:
	i = GPIO.input(4)
	if i == 0:
		os.system("python test.py")