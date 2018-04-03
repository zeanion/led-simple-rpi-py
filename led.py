import RPi.GPIO as GPIO
import time
import sys

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

LED1    = 11

GPIO.setup(LED1,GPIO.OUT)

try:
	while True:
		print "LED turned ON"
		GPIO.output(LED1,GPIO.HIGH)
		time.sleep(0.3)
		print "LED turned OFF"
		GPIO.output(LED1,GPIO.LOW)
		time.sleep(0.3)

except KeyboardInterrupt:
	GPIO.cleanup()

except:
	print "Something went wrong!", sys.exc_info()[0]
	GPIO.cleanup()