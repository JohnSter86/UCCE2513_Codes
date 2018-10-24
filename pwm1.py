import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

p = GPIO.PWM(17, 50)
p.start(0)
while True:
	try:
		for dc in range(0, 101, 5):
			p.ChangeDutyCycle(dc)
			time.sleep(0.1)
		for dc in range(100, -1, -5):
			p.ChangeDutyCycle(dc)
			time.sleep(0.1)
	except KeyboardInterrupt:
		p.stop()
		GPIO.cleanup()
		exit()
